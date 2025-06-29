# ===================================================================================================
# Imports: External
# ===================================================================================================
import wx
import os

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
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

    def _init_ui(self):
        '''
        Initialses the UI, updating and overriding any properties
        '''
        self.clear_slots()
        self.add_slot()

    # ===================================================================================================
    # Event Handles
    # ===================================================================================================
    def _on_start_conversion(self, event):
        '''
        Handler: Start Conversion

        :param event: wx Btn Event
        :type event: wx.Event
        '''

        self.text_output_log.Clear()
        self.write_to_log("[+] Starting conversion process")

        # Process Inputs
        output_dir = self.dp_outputdir.GetPath()

        # ===================================================================================================
        # Validate Inputs
        # ===================================================================================================
        # Validate output directory
        if not os.path.isdir(output_dir):
            self.write_to_log("ERROR: Output Directory must be set to a valid folder path")
            return


    # ===================================================================================================
    # Helpers
    # ===================================================================================================
    def clear_slots(self, event=None):
        '''
        Clears all slots from the slot table

        :param event: Button event, if called from a click
        :type event: wx.Event
        '''
        self.sb_slots.Clear(True)
        self.sb_slots.Layout()
        self.write_to_log("Clearing Slots")

    def delete_slot(self, slot):
        '''
        Deletes a Slot from the Input Map table
        :param slot:
        :return:
        '''

        self.sb_slots.Detach(slot)


    def add_slot(self, event=None):
        '''
        Adds a new slot to the slot table

        :param event: Button event, if called from a click
        :type event: wx.Event
        '''
        slot = InputMapSlot(self.slots_scrollbox)
        self.sb_slots.Add(slot, 0, wx.EXPAND)
        self.slots_scrollbox.Layout()
        self.slots_scrollbox.FitInside()
        self.write_to_log("[+] Slot Added")

    def write_to_log(self, msg):
        '''
        Writes a message to the Output Log

        :param msg: The message to write
        :type msg: str
        '''
        log_msg = "%s\n" % msg
        self.text_output_log.write(log_msg)





