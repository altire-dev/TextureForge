# ===================================================================================================
# Imports: External
# ===================================================================================================
import wx
import os
import time
import json
from threading import Thread
from threading import Event

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
from .input_map_slot import InputMapSlot
from textureforge.converters import DDSConverter
from textureforge.converters import ConversionOperation
from textureforge.processors import DDSProcessor
from textureforge.components.image_discovery import ImageDiscoverer
from textureforge.utils import utils
from textureforge.components import game_presets

from .abs_tab_dds_converter import AbsTFTabDDSConverter

# ===================================================================================================
# TF Tab: DDS Converter
# ===================================================================================================
class TFTabDDSConverter(AbsTFTabDDSConverter):
    '''
    Texture Forge Tab: DDS Converter
    '''


    # ===================================================================================================
    # Properties
    # ===================================================================================================

    # ===================================================================================================
    # Methods
    # ===================================================================================================
    def __init__(self, tfgui, parent):
        '''
        Constructor

        :param: tfgui: The TextureForge GUI instance
        :type tfgui: TextureFrogeGUI
        :param parent: The Tab's parent Notebook
        :type parent: wx.Notebook
        '''
        self._tfgui = tfgui
        self._columns = {}
        self._slots = []
        self._project_file = None
        self._count_maps_converted = 0
        self._dds_converter = None
        self._auto_converter = None
        self._game_preset = None

        # Initialise Frame
        super(TFTabDDSConverter, self).__init__(parent)

        # Set up GUI
        self._bind_events()
        self._init_ui()

    def _bind_events(self):
        '''
        Binds GUI Events
        '''

        # Button events
        self.Bind(wx.EVT_BUTTON, self._on_start_conversion, self.btn_convert)

        # Button Events - Slot Management
        self.Bind(wx.EVT_BUTTON, self.clear_slots, self.btn_clear_slots)
        self.Bind(wx.EVT_BUTTON, self.add_slot, self.btn_add_slot)

        # Button Events - Project
        self.Bind(wx.EVT_BUTTON, self._on_new, self.btn_new)
        self.Bind(wx.EVT_BUTTON, self._on_save, self.btn_save)
        self.Bind(wx.EVT_BUTTON, self._on_save_as, self.btn_save_as)
        self.Bind(wx.EVT_BUTTON, self._on_load, self.btn_load)
        self.Bind(wx.EVT_BUTTON, self._on_scan_folder, self.btn_scan_folder)
        self.Bind(wx.EVT_BUTTON, self._on_open_output_dir, self.btn_open_output_dir)
        self.Bind(wx.EVT_BUTTON, self._on_auto_convert, self.btn_autoconvert)
        self.Bind(wx.EVT_CHOICE, self._on_preset_change, self.choice_game_preset)

        # File/Dir Change Events
        self.Bind(wx.EVT_DIRPICKER_CHANGED, self._on_output_dir_changed, self.dp_outputdir)

    def _init_ui(self):
        '''
        Initialses the UI, updating and overriding any properties
        '''
        self._game_preset = game_presets.GP_NONE

        # ============================================================================================================
        # Store Columns
        # ============================================================================================================
        self._columns["enabled"]        = self.col_enabled
        self._columns["texture_path"]   = self.col_texture_path
        self._columns["compression"]    = self.col_compression
        self._columns["status"]         = self.col_status
        self._columns["actions"]        = self.col_actions

        # ============================================================================================================
        # Initialise Slots
        # ============================================================================================================

        self.clear_slots()
        self.add_slot()
        self.text_output_log.Clear()

    # ===================================================================================================
    # Event Handles
    # ===================================================================================================
    def _on_preset_change(self, event=None):
        '''
        Handler: Game Preset changed

        :param event: The wx Button event
        :type event. wx.Event
        '''
        self._game_preset = self.choice_game_preset.GetStringSelection()

        # Update Preset for slots
        for slot in self.get_slots():
            slot.set_game_preset(self._game_preset)

    def on_close(self):
        '''
        Handler: Application closed
        '''
        if self._auto_converter:
            self._auto_converter.stop()
        if self._dds_converter:
            self._dds_converter.stop()

    def _on_auto_convert(self, event):
        '''
        Handler: Auto-convert button pressed

        :param event: wx Btn Event
        :type event: wx.Event
        '''
        # ===================================================================================================
        # Enable Auto Conversion
        # ===================================================================================================
        if not self._auto_converter:
            # Validate Input
            output_dir = self.dp_outputdir.GetPath()
            if not os.path.isdir(output_dir):
                self.write_to_log("Output Directory must first be set to a valid folder path", True)
                return
            if not self.get_valid_slots():
                self.write_to_log("At least one slot must be configured and enabled to perform conversion")
                return

            # Update UI
            for slot in self.get_slots():
                if slot.is_enabled() and slot.is_path_valid():
                    slot.set_status(slot.STATUS_WATCHING)
                else:
                    slot.set_status(slot.STATUS_DISABLED)
            self.btn_load.Disable()
            self.btn_save.Disable()
            self.btn_save_as.Disable()
            self.text_project_name.Disable()
            self.btn_convert.Disable()
            self.btn_autoconvert.SetBackgroundColour(wx.Colour(46, 197, 53))
            self.btn_autoconvert.SetLabel("AUTO CONVERSION RUNNING")
            self.panel_input_maps.Disable()
            self.dp_outputdir.Disable()
            self.choice_game_preset.Disable()
            self.btn_scan_folder.Disable()

            '''
            Every second, run through eah slot
                Check if file hash has changed and thus file has been updated
                if so, perform conversion and write to log
                Get the file hash of each file and store it
            '''
            self._auto_converter = DDSAutoConverter(self, output_dir)
            self._auto_converter.start()

        # ===================================================================================================
        # Disable Auto Conversion
        # ===================================================================================================
        else:
            self.btn_autoconvert.Disable()
            self._auto_converter.stop()


    def on_auto_convert_stopped(self):
        '''
        Handler: Auto-conversion stopped
        '''
        # Update UI
        self.btn_load.Enable()
        self.btn_save.Enable()
        self.btn_save_as.Enable()
        self.text_project_name.Enable()
        self.btn_convert.Enable()
        self.btn_autoconvert.Enable()
        self.btn_autoconvert.SetForegroundColour(wx.Colour(0, 0, 0, 255))
        self.btn_autoconvert.SetBackgroundColour(wx.Colour(253, 253, 253, 255))
        self.btn_autoconvert.SetLabel("ENABLE AUTO CONVERSION")
        self.panel_input_maps.Enable()
        self.dp_outputdir.Enable()
        self.btn_scan_folder.Enable()
        self.choice_game_preset.Enable()
        for slot in self.get_slots():
            slot.set_status(slot.STATUS_WAITING)

        self._auto_converter = None
        self.write_to_log("Auto-conversion stopped")

    def _on_scan_folder(self, event):
        '''
        Handler: Scan Folder button pressed

        :param event: wx Btn Event
        :type event: wx.Event
        '''

        # Open Load Modal
        with wx.DirDialog(
                self, "Select Target Folder",
                style=wx.DIRP_DEFAULT_STYLE | wx.DIRP_DIR_MUST_EXIST
        ) as dir_dialog:
            # Dialog cancelled
            if dir_dialog.ShowModal() == wx.ID_CANCEL:
                return
            dir_path = dir_dialog.GetPath()

        # ===================================================================================================
        # Perform Save
        # ===================================================================================================
        self.write_to_log("Scanning Directory: %s" % dir_path)
        self.scan_dir(dir_path)


    def _on_output_dir_changed(self, event=None):
        '''
        Handler: Output Directory changed

        :param event: wx Btn Event
        :type event: wx.Event
        '''
        output_dir = self.dp_outputdir.GetPath()
        if os.path.isdir(output_dir):
            self.btn_open_output_dir.Enable()
        else:
            self.btn_open_output_dir.Disable()
        self.dp_outputdir.GetTextCtrl().SetInsertionPointEnd()


    def _on_open_output_dir(self, event):
        '''
        Handler: Open Output Directory buttion clicked

        :param event: wx Btn Event
        :type event: wx.Event
        '''
        output_dir = self.dp_outputdir.GetPath()
        utils.open_explorer(output_dir)

    def _on_stop_conversion(self, event):
        '''
        Handler: Stop Conversion

        :param event: wx Btn Event
        :type event: wx.Event
        '''
        if self._dds_converter:
            self._dds_converter.stop()

    def on_conversion_cancelled(self):
        '''
        Handler: Conversion was cancelled by the user
        '''
        self.on_conversion_finished(True)
        self.progressbar.SetValue(0)

    def _on_start_conversion(self, event):
        '''
        Handler: Start Conversion

        :param event: wx Btn Event
        :type event: wx.Event
        '''

        # ===================================================================================================
        # Validate Inputs
        # ===================================================================================================
        # Validate output directory
        output_dir = self.dp_outputdir.GetPath()
        if not os.path.isdir(output_dir):
            self.write_to_log("Output Directory must first be set to a valid folder path", True)
            return
        # Validate Slots
        if not self.get_valid_slots():
            self.write_to_log("At least one slot must be configured and enabled to perform conversion")
            return

        # ===================================================================================================
        # Update UI
        # ===================================================================================================
        self.Unbind(wx.EVT_BUTTON, self.btn_convert)
        self.Bind(wx.EVT_BUTTON, self._on_stop_conversion, self.btn_convert)
        self.btn_convert.SetLabel("CANCEL")
        self.text_output_log.Clear()
        self.progressbar.SetValue(0)
        self.write_to_log("Starting conversion process")
        for slot in self.get_slots():
            slot.set_status(slot.STATUS_WAITING)

        # ===================================================================================================
        # Process Slots
        # ===================================================================================================
        slots = self.get_slots()
        target_maps = []
        for slot in slots:
            if not slot.is_enabled():
                continue

            texture_path    = slot.get_texture_path()
            compression     = slot.get_compression_type()
            target_maps.append((texture_path, compression, slot))

        self.progressbar.SetRange(len(target_maps))
        self._dds_converter = DDSConverter(self, output_dir, target_maps)
        self._dds_converter.start()

    def on_map_converted(self, slot):
        '''
        Handler: Texture Map successfully converted

        :param slot: The Slot of the Texture Map that was converted
        :type slot: InputMapSlot
        '''
        self._count_maps_converted += 1
        self.progressbar.SetValue(self._count_maps_converted)

    def on_conversion_finished(self, cancelled=False):
        '''
        Handler: DDS Conversion has finished

        :param cancelled: Whether the operation was cancelled or not
        :type cancelled: bool
        '''
        self.Unbind(wx.EVT_BUTTON, self.btn_convert)
        self.Bind(wx.EVT_BUTTON, self._on_start_conversion, self.btn_convert)
        self.btn_convert.SetLabel("CONVERT")
        if cancelled:
            self.write_to_log("Conversion cancelled")
        else:
            self.write_to_log("Conversion finished")

    def _on_save(self, event):
        '''
        Handler: Project Save Button clicked

        :param event: Button event
        :type event: wx.Event
        '''

        # ===================================================================================================
        # Validate Input
        # ===================================================================================================
        project_name = self.text_project_name.GetValue()
        if not project_name:
            self.write_to_log("Project name must be set", True)
            return
        output_dir = self.dp_outputdir.GetPath()

        # ===================================================================================================
        # Perform Save
        # ===================================================================================================
        self.save_project(self._project_file)

    def _on_save_as(self, event):
        '''
        Handler: Project Save As Button clicked

        :param event: Button event
        :type event: wx.Event
        '''
        save_path = None

        # Open Save Modal
        with wx.FileDialog(
            self, "Save Project",
            wildcard="TextureForge Project (*.tfp)|*.tfp",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        ) as file_dialog:
            # Dialog cancelled
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            save_path = file_dialog.GetPath()

        # ===================================================================================================
        # Validate Input
        # ===================================================================================================
        project_name = self.text_project_name.GetValue()
        if not project_name:
            self.write_to_log("Project name must be set", True)
            return
        output_dir = self.dp_outputdir.GetPath()

        # ===================================================================================================
        # Perform Save
        # ===================================================================================================
        self.save_project(save_path)

    def _on_load(self, event):
        '''
        Handler: Project Load Button clicked

        :param event: Button event
        :type event: wx.Event
        '''
        file_path = None

        # Open Load Modal
        with wx.FileDialog(
                self, "Select Project File",
                wildcard="TextureForge Project (*.tfp)|*.tfp",
                style=wx.FD_OPEN | wx.FLP_FILE_MUST_EXIST
        ) as file_dialog:
            # Dialog cancelled
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            file_path = file_dialog.GetPath()

        # ===================================================================================================
        # Perform Save
        # ===================================================================================================
        self.load_project(file_path)

    def _on_new(self, event):
        '''
        Handler: New Project Button clicked

        :param event: wx Button Event
        :type event: wx.Event
        '''

        # Clear Input Data
        self.text_project_name.Clear()
        self.dp_outputdir.SetPath("")
        self.clear_slots()

        # Update Log
        self.add_slot()
        self.text_output_log.Clear()
        self.write_to_log("New Project Initialised")

    def on_slot_deleted(self, slot):
        '''
        Handler: A specific slot was deleted

        :param slot: The slot that was deleted
        :type slot: InputMapSlot
        '''
        self._slots.remove(slot)
        self.write_to_log("Slot deleted")

    # ===================================================================================================
    # Helpers
    # ===================================================================================================
    def scan_dir(self, path):
        '''
        Scans a directory for image files to load

        :param path: The path to the directory to scan
        :type path: str
        '''
        id = ImageDiscoverer()

        # Find directories
        image_files = id.search_directory(path)
        if len(image_files) == 0:
            self.write_to_log("No images found in target directory")
            return

        self.clear_slots()
        for image_file in image_files:
            slot = self.add_slot()
            slot.set_texture_path(image_file)

        self.write_to_log("%s image(s) found" % len(image_files))




    def save_project(self, path):
        '''
        Saves the project data to the specified path
        
        :param path: Path to the target save file
        :type path: str
        '''
        
        # ===================================================================================================
        # Build Save Data
        # ===================================================================================================
        save_data = {
            "save_version": "2",
            "project_name": self.text_project_name.GetValue(),
            "output_dir": self.dp_outputdir.GetPath(),
            "game_preset": self.choice_game_preset.GetStringSelection(),
            "slots": []
        }

        # ===================================================================================================
        # Populate Slot data
        # ===================================================================================================
        for slot in self.get_slots():
            slot_data = {
                "enabled": slot.is_enabled(),
                "texture_path": slot.get_texture_path(),
                "compression": slot.get_compression_type()
            }
            save_data["slots"].append(slot_data)

        with open(path, "w") as save_file:
            json.dump(save_data, save_file)

        self.set_project_file(path)
        self.write_to_log("Project Saved: %s --> %s" % (save_data["project_name"], path))

    def load_project(self, path):
        '''
        Loads project data from the TextureForge project file at the specified location

        :param path: Path to the TextureForge project file to load
        :type path: str
        '''
        self.write_to_log("Loading project file: %s" % path)

        # ===================================================================================================
        # Read File
        # ===================================================================================================
        try:
            with open(path, "r") as project_file:
                project_data = json.load(project_file)
        except Exception as ex:
            self.write_to_log("Unable to load project at %s --> %s" % (path, ex))
            return

        # ===================================================================================================
        # Load Project Settings
        # ===================================================================================================
        self.text_project_name.SetValue(project_data["project_name"])
        self.dp_outputdir.SetPath(project_data["output_dir"])
        self._on_output_dir_changed()
        if int(project_data["save_version"]) > 1:
            self.choice_game_preset.SetStringSelection(project_data["game_preset"])

        # ===================================================================================================
        # Load Slots
        # ===================================================================================================
        self.clear_slots()
        for slot_data in project_data["slots"]:
            slot = self.add_slot()
            slot.set_enabled(slot_data["enabled"])
            slot.set_texture_path(slot_data["texture_path"], False)
            slot.set_compression_selection(slot_data["compression"])

        # Update Slot Texture Path controls (cursor to end)
        for slot in self.get_slots():
            slot.fp_texture_path.Layout()
            slot.fp_texture_path.GetTextCtrl().SetInsertionPointEnd()

        self._on_preset_change()
        self.set_project_file(path)
        self.write_to_log("Project Loaded: %s" % path)

        
    def clear_slots(self, event=None):
        '''
        Clears all slots from the slot table

        :param event: Button event, if called from a click
        :type event: wx.Event
        '''
        self.write_to_log("Clearing Slots")

        for column in self._columns:
            self._columns[column].Clear(True)

        self.slots_table.Layout()
        self._slots.clear()

    def add_slot(self, event=None):
        '''
        Adds a new slot to the slot table

        :param event: Button event, if called from a click
        :type event: wx.Event
        :returns: The newly added slot instance
        :rtype: InputMapSlot
        '''
        slot = InputMapSlot(self, self.slots_table, self._columns)
        slot.set_compression_options(DDSProcessor.COMPRESSION_FORMATS)
        slot.set_game_preset(self._game_preset)
        self.write_to_log("Slot Added")
        self._slots.append(slot)
        return slot

    def get_slots(self):
        '''
        Gets the Input Map Slots

        :return: The current Input Map Slots
        :rtype: list[InputMapSlot]
        '''
        return self._slots

    def get_valid_slots(self, enabled_only=True):
        '''
        Returns the currently valid slots (Texture Path set)

        :param enabled_only: whether only enabled slots should be considered. Defaults to True
        :type enabled_only: bool
        '''
        valid_slots = []
        for slot in self.get_slots():
            try:
                if slot.is_enabled() and os.path.isfile(slot.get_texture_path()):
                    valid_slots.append(slot)
            except RuntimeError:
                continue
        return valid_slots

    def write_to_log(self, msg, error=False):
        '''
        Writes a message to the Output Log

        :param msg: The message to write
        :type msg: str
        '''
        log_msg = "[%s] " % utils.get_datetime_string()
        if error:
            log_msg += "ERROR: "
        log_msg += "%s\n" % msg
        self.text_output_log.write(log_msg)

    def set_project_file(self, path):
        '''
        Sets the path to the project file for the current project

        :param path: Path to the TextureForge project file (DDS Converter)
        :type path: str
        '''
        self._project_file = path
        project_filename = utils.get_path_filename(path)
        self._tfgui.set_title_context("%s (%s)" % (self.text_project_name.GetValue(), project_filename))
        self.btn_save.Enable()

    def _get_icon_path(self):
        '''
        Gets the path to the GUI Icon (.ico) file

        :return: The path to the GUI Icon File
        :rtype: str
        '''
        icon_path = None
        tf_root = utils.get_tf_root_path()

        if "_MEI" in __file__: # (Packed)
            icon_path = os.path.join(
                os.path.dirname(tf_root), "resources", "icon.ico"
            )
        else: # (Not Packed)
            icon_path = os.path.join(tf_root, "resources", "icon.ico")

        return icon_path



# ===================================================================================================
# Auto-Converter Class
# ===================================================================================================
class DDSAutoConverter(Thread):
    '''
    DDS Auto-Converter Thread
    '''

    # ===================================================================================================
    # Properties
    # ===================================================================================================

    # ===================================================================================================
    # Methods
    # ===================================================================================================
    def __init__(self, tab, output_dir):
        '''
        Constructor

        :param tab: The DDS converter Tab instance
        :type tab: TFTabDDSConverter
        :param output_dir: Path to the output directory
        :type output_dir: str
        '''
        self._tab = tab
        self._output_dir = output_dir
        self._stop_event = Event()
        super(DDSAutoConverter, self).__init__()


    def stop(self):
        '''
        Stops the auto-conversion process
        '''
        self._stop_event.set()

    def run(self):
        '''
        DDS Auto Converter - Thread runner
        '''
        valid_slots = {}

        # Get Initial modtimes
        for slot in self._tab.get_valid_slots():
            valid_slots[slot] = os.path.getmtime(slot.get_texture_path())

        # ===================================================================================================
        # Main Watcher Loop
        # ===================================================================================================
        self._tab.write_to_log("Auto-conversion running. Watching for file changes...")
        while not self._stop_event.isSet():
            maps_to_convert = []
            time.sleep(1)

            # Check for changes
            slots = self._tab.get_valid_slots()
            for slot in slots:
                tpath = slot.get_texture_path()
                mod_time = os.path.getmtime(tpath)
                if mod_time > valid_slots[slot]:
                    self._tab.write_to_log("File change detected --> %s" % tpath)
                    maps_to_convert.append((tpath, slot.get_compression_type(), slot))
                    valid_slots[slot] = mod_time

            # Convert Updated Maps
            if maps_to_convert:
                dds_processor = DDSProcessor()
                for map in maps_to_convert:
                    path, compression, slot = map[0], map[1], map[2]

                    # Check Stop Event
                    if self._stop_event.isSet():
                        break

                    # !!! Convert !!!
                    filename = utils.get_path_filename(path)
                    self._tab.write_to_log("Converting Map: %s" % filename)
                    dds_processor.convert_to_dds(path, self._output_dir, compression)
                    self._tab.write_to_log("Map converted")

        self._tab.on_auto_convert_stopped()


