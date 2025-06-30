# ===================================================================================================
# Import: External
# ===================================================================================================
import wx
from wx import Colour

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
from .abs_gui import AbsInputMapSlot

# ===================================================================================================
# Input Map Table Slot Class
# ===================================================================================================
class InputMapSlot(AbsInputMapSlot):
    '''
    Input Map Table Slot
    '''


    # ==================================================================================================
    # Properties
    # ==================================================================================================
    STATUS_WAITING      = 0
    STATUS_IN_PROGRESS  = 1
    STATUS_COMPLETE     = 2
    STATUS_FAILED       = 3

    COLOR_DEFAULT       = Colour(0, 0, 0)
    COLOR_IN_PROGRESS   = Colour(255, 204, 102)
    COLOR_COMPLETE      = Colour(0, 153, 0)
    COLOR_FAILED        = Colour(255, 26, 26)

    # ==================================================================================================
    # Methods
    # ==================================================================================================
    def __init__(self, tf, parent):
        '''
        Constructor

        :param tf: The Texture Forge GUI instance
        :type: TextureForgeGUI
        :param parent: Parent Window/Panel
        :type parent: wx.Window
        '''
        self._tf = tf
        self._compression_formats = []
        super(InputMapSlot, self).__init__(parent)
        self.bind_events()


    def bind_events(self):
        '''
        Binds slot events
        '''

        self.Bind(wx.EVT_BUTTON, self._on_delete, self.btn_delete)

    # ===================================================================================================
    # Setters
    # ===================================================================================================
    def set_compression_options(self, formats):
        '''
        Sets the available compression format options

        :param formats: dict of available compression formats
        :type formats: dict
        '''
        self.choice_compression.Clear()

        # Process Compression Formats
        for format_name in formats:
            self._compression_formats.append(format_name)
            self.choice_compression.Append(formats[format_name]["display_name"])
        self.choice_compression.SetSelection(0)

    def set_status(self, status):
        '''
        Sets the Conversion status

        :param status: The new status
        :type status: int
        '''
        if status == self.STATUS_WAITING:
            self.label_status.SetLabel("Waiting")
            self.label_status.SetForegroundColour(self.COLOR_DEFAULT)
        elif status == self.STATUS_IN_PROGRESS:
            self.label_status.SetLabel("In Progress")
            self.label_status.SetForegroundColour(self.COLOR_IN_PROGRESS)
        elif status == self.STATUS_COMPLETE:
            self.label_status.SetLabel("Complete")
            self.label_status.SetForegroundColour(self.COLOR_COMPLETE)
        elif status == self.STATUS_FAILED:
            self.label_status.SetLabel("Failed")
            self.label_status.SetForegroundColour(self.COLOR_FAILED)

    def set_texture_path(self, path):
        '''
        Sets the slot's Texture Path

        :param path: The path to use
        :type path: str
        '''
        self.fp_map_path.SetPath(path)

    def set_compression_selection(self, _type):
        '''
        Sets the slot's Compression Type selection

        :param: _type: The compression type to use
        :type _type: str
        '''
        idx = self._compression_formats.index(_type)
        self.choice_compression.SetSelection(idx)

    def set_enabled(self, enabled):
        '''
        Sets the slots's enabled status

        :param enabled: The slot's new enabled status
        :type enabled: bool
        '''
        self.cb_enabled.SetValue(enabled)

    # ===================================================================================================
    # Getters
    # ===================================================================================================
    def is_enabled(self):
        '''
        Checks if the slot is enabled

        :return: True if enabled, otherwise False
        :rtype: bool
        '''
        return self.cb_enabled.GetValue()

    def get_texture_path(self):
        '''
        Gets the slots Texture Path

        :return: The slots texture path
        :rtype: str
        '''
        return self.fp_map_path.GetPath()

    def get_compression_type(self):
        '''
        Gets the selected compression type

        :return: The currently selected compression type
        :rtype: str
        '''
        idx = self.choice_compression.GetSelection()
        return self._compression_formats[idx]

    # ===================================================================================================
    # Event Handlers
    # ===================================================================================================
    def _on_delete(self, event):
        '''
        Slot deletion handler

        :param event: The Delete Button Event
        :type event: wx.Event
        '''
        self._tf.delete_slot(self)
