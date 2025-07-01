# ===================================================================================================
# Imports: External
# ===================================================================================================
import wx
import os
import time
import json

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
from ..converters import DDSConverter
from ..converters import ConversionOperation
from ..processors import DDSProcessor
from .input_map_slot import InputMapSlot
from textureforge.gui.abs_gui import TextureForgeMF

# ===================================================================================================
# Texture Forge GUI Class
# ===================================================================================================
class TextureForgeGUI(TextureForgeMF):
    '''
    Texture Forge GUI
    '''


    # ===================================================================================================
    # Properties
    # ===================================================================================================


    # ===================================================================================================
    # Methods
    # ===================================================================================================
    def __init__(self, version, author):
        '''
        Constructor

        :param version: The app version
        :type version: str
        :param author: The app author
        :type author: str
        '''
        self._version = version
        self._author = author
        self._columns = {}
        self._slots = []

        # Initialise Frame
        super(TextureForgeGUI, self).__init__(None)

        # Set up GUI
        self._bind_events()
        self._init_ui()

    def _bind_events(self):
        '''
        Binds GUI Events
        '''

        # Bind button events
        self.Bind(wx.EVT_BUTTON, self._on_start_conversion, self.btn_convert)
        self.Bind(wx.EVT_BUTTON, self.clear_slots, self.btn_clear_slots)
        self.Bind(wx.EVT_BUTTON, self.add_slot, self.btn_add_slot)
        self.Bind(wx.EVT_BUTTON, self._on_save_project, self.btn_save_project)
        self.Bind(wx.EVT_BUTTON, self._on_load_project, self.btn_load_project)

    def _init_ui(self):
        '''
        Initialses the UI, updating and overriding any properties
        '''

        self.SetTitle("TextureForge v%s" % self._version)

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

        # =================================
        # TEST
        # =================================
        # self.dp_outputdir.SetPath(".\\")
        # slots = self.get_slots()
        # slots[0].set_texture_path("C:\\OneDrive\\dev\\Skyrim\\projects\\Lordbound\\projects\\garshakur\\assets\\archway\\exports\\textures\\archway_trim_metal_m.png")
        # slots[0].set_texture_path(r"F:\OneDrive\dev\Skyrim\projects\Lordbound\projects\garshakur\assets\archway\exports\textures\\archway_trim_metal_d.png")
        # slots[0].set_compression_selection("BC1_UNORM")

    # ===================================================================================================
    # Event Handles
    # ===================================================================================================
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
            self.write_to_log("ERROR: Output Directory must be set to a valid folder path")
            return

        # ===================================================================================================
        # Update UI
        # ===================================================================================================
        self.btn_convert.SetLabel("CANCEL")
        self.text_output_log.Clear()
        self.write_to_log("[+] Starting conversion process")
        for slot in self.get_slots():
            slot.set_status("Waiting")

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
            if not os.path.isfile(texture_path):
                self.write_to_log("[!!] Texture path file is invalid, or does not exist: %s" % texture_path)
                return

            target_maps.append((texture_path, compression, slot))

        dds_converter = DDSConverter(self, output_dir, target_maps)
        dds_converter.start()

    def on_map_converted(self, slot):
        '''
        Handler: Texture Map successfully converted

        :param slot: The Slot of the Texture Map that was converted
        :type slot: InputMapSlot
        '''
        pass

    def on_conversion_finished(self):
        '''
        Handler: DDS Conversion has finished
        '''
        self.btn_convert.SetLabel("CONVERT")
        self.write_to_log("[+] Conversion Finished")


    def _on_save_project(self, event):
        '''
        Handler: Project Save Button clicked

        :param event: Button event
        :type event: wx.Event
        '''
        save_path = None

        # Open Save Modal
        with wx.FileDialog(
            self, "Save Project",
            wildcard="TextureForge Project File (*.tfp)|*.tfp",
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
            self.write_to_log("ERROR: Project name must be set")
            return
        output_dir = self.dp_outputdir.GetPath()

        # ===================================================================================================
        # Perform Save
        # ===================================================================================================
        self.save_project(save_path)

    def _on_load_project(self, event):
        '''
        Handler: Project Load Button clicked

        :param event: Button event
        :type event: wx.Event
        '''
        file_path = None

        # Open Load Modal
        with wx.FileDialog(
                self, "Select Project File",
                wildcard="TextureForge Project File (*.tfp)|*.tfp",
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


    # ===================================================================================================
    # Helpers
    # ===================================================================================================
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
            "save_version": "1",
            "project_name": self.text_project_name.GetValue(),
            "output_dir": self.dp_outputdir.GetPath(),
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
        with open(path, "r") as project_file:
            project_data = json.load(project_file)

        # ===================================================================================================
        # Load Project Settings
        # ===================================================================================================
        self.text_project_name.SetValue(project_data["project_name"])
        self.dp_outputdir.SetPath(project_data["output_dir"])

        # ===================================================================================================
        # Load Slots
        # ===================================================================================================
        self.clear_slots()
        for slot_data in project_data["slots"]:
            slot = self.add_slot()
            slot.set_enabled(slot_data["enabled"])
            slot.set_texture_path(slot_data["texture_path"])
            slot.set_compression_selection(slot_data["compression"])

        
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

    def on_slot_deleted(self, slot):
        '''
        Handler: A specific slot was deleted
        :param slot: The slot that was deleted
        :type slot: InputMapSlot
        '''
        self._slots.remove(slot)
        self.write_to_log("Slot deleted")

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
        self.write_to_log("[+] Slot Added")
        self._slots.append(slot)
        return slot

    def get_slots(self):
        '''
        Gets the Input Map Slots

        :return: The current Input Map Slots
        :rtype: list[InputMapSlot]
        '''
        return self._slots

    def write_to_log(self, msg):
        '''
        Writes a message to the Output Log

        :param msg: The message to write
        :type msg: str
        '''
        log_msg = "%s\n" % msg
        self.text_output_log.write(log_msg)





