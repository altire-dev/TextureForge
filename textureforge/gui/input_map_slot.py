# ===================================================================================================
# Imports: External
# ===================================================================================================
import wx
from wx import CheckBox
from wx import FilePickerCtrl

# ===================================================================================================
# Input Map Slot Class
# ===================================================================================================
class InputMapSlot:
    '''
    Texture Map Table Slot
    '''

    # ===================================================================================================
    # Properties
    # ===================================================================================================
    MIN_CELL_SIZE = wx.Size(-1, 35)

    # Status Enum
    STATUS_WAITING      = 0
    STATUS_IN_PROGRESS  = 1
    STATUS_COMPLETE     = 2
    STATUS_FAILED       = 3
    STATUS_DISABLED     = 4

    # Status Labels
    STATUS_LABELS = {
        STATUS_WAITING: "Waiting",
        STATUS_IN_PROGRESS: "In Progress",
        STATUS_COMPLETE: "Complete",
        STATUS_FAILED: "Failed",
        STATUS_DISABLED: "Disabled"
    }

    # Colours
    COLOR_DEFAULT       = wx.Colour(0, 0, 0)
    COLOR_IN_PROGRESS   = wx.Colour(255, 204, 102)
    COLOR_COMPLETE      = wx.Colour(0, 153, 0)
    COLOR_FAILED        = wx.Colour(255, 26, 26)
    COLOR_DISABLED      = wx.Colour(100, 100, 100)

    # ============================================================================================================
    # Methods
    # ============================================================================================================
    def __init__(self, tf, table, cols):
        '''
        Constructor

        :param tf: The TextureForge instance
        :type tf: TextureForge
        :param table: The slots table panel
        :type table: wx.Panel
        :param cols: The table columns
        :type cols: dict[str, wx.Sizer]
        '''
        self._tf = tf
        self._table = table
        self._cols = cols
        self._cells = []
        self._compression_formats = []

        # ===================================================================================================
        # Build Components
        # ===================================================================================================
        # Enabled (Checkbox)
        self.cb_enabled = CheckBox(self._table, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, size=self.MIN_CELL_SIZE)
        self._cols["enabled"].Add(self.cb_enabled, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        # Texture Path (FilePicker)
        self.fp_texture_path = FilePickerCtrl(self._table, wx.ID_ANY, wx.EmptyString, "Select Image File", wildcard="PNG File|*.png")
        self._create_cell(self.fp_texture_path, self._cols["texture_path"], 0)

        # Compression (ChoiceBox)
        self.choice_compression = wx.Choice(self._table, wx.ID_ANY, wx.DefaultPosition)
        self._create_cell(self.choice_compression, self._cols["compression"], 0)

        # Status (StaticText)
        self._label_status = wx.StaticText(self._table, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0)
        self._label_status.Wrap( -1 )
        self._create_cell(self._label_status, self._cols["status"], 0)

        # Actions (Buttons)
        self.btn_delete = wx.Button(self._table, wx.ID_ANY, "Delete", wx.DefaultPosition)
        self._create_cell(self.btn_delete, self._cols["actions"], 0)

        self.set_status(self.STATUS_WAITING)
        self.cb_enabled.SetValue(True)
        self.set_enabled(True)

        self._table.Layout()

        self.bind_events()

    def bind_events(self):
        '''
        Binds GUI Events
        '''
        self._table.Bind(wx.EVT_BUTTON, self._on_delete, self.btn_delete)
        self._table.Bind(wx.EVT_FILEPICKER_CHANGED, self._on_texture_path_changed, self.fp_texture_path)
        self._table.Bind(wx.EVT_CHECKBOX, self._on_enabled_change, self.cb_enabled)

    # ============================================================================================================
    # Event Handlers/Callbacks
    # ============================================================================================================
    def _on_enabled_change(self, event):
        '''
        Handler: Enabled Checkbox state changed
        '''

        if self.cb_enabled.GetValue():
            self.enable_slot()
        else:
            self.disable_slot()

    def _on_delete(self, event=None):
        '''
        Handler: Delete button clicked for slot

        :param event: The wx Button event
        :type event. wx.Event
        '''
        self._cols["enabled"].Detach(self.cb_enabled)
        self._cols["texture_path"].Detach(self.fp_texture_path)
        self._cols["compression"].Detach(self.choice_compression)
        self._cols["status"].Detach(self._label_status)
        self._cols["actions"].Detach(self.btn_delete)

        self.cb_enabled.Destroy()
        self.fp_texture_path.Destroy()
        self.choice_compression.Destroy()
        self._label_status.Destroy()
        self.btn_delete.Destroy()

        self._tf.on_slot_deleted(self)
        self._table.Layout()


    def _on_texture_path_changed(self, event=None):
        '''
        Handler: Texture Path changed

        :param event: The wx Button event
        :type event. wx.Event
        '''

        # Move cursor to end
        self.fp_texture_path.GetTextCtrl().SetInsertionPointEnd()

    # ============================================================================================================
    # Getters
    # ============================================================================================================
    def is_enabled(self):
        '''
        Checks if the slot is enabled

        :returns: True if enabled, otherwise False
        :rtype: bool
        '''
        return self.cb_enabled.GetValue()

    def get_texture_path(self):
        '''
        Gets the slots Texture Path

        :return: The slots texture path
        :rtype: str
        '''
        return self.fp_texture_path.GetPath()

    def get_compression_type(self):
        '''
        Gets the selected compression type

        :return: The currently selected compression type
        :rtype: str
        '''
        idx = self.choice_compression.GetSelection()
        return self._compression_formats[idx]

    def enable_slot(self):
        '''
        Enables the slot
        '''
        self.set_status(self.STATUS_WAITING)
        self.fp_texture_path.Enable()
        self.choice_compression.Enabl()

    def disable_slot(self):
        '''
        Disables the slot
        '''
        self.set_status(self.STATUS_DISABLED)
        self.fp_texture_path.Disable()
        self.choice_compression.Disable()

    # ============================================================================================================
    # Setters
    # ============================================================================================================
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
        Sets the conversion status for this slot

        :param status: The new status
        :type status: int
        '''
        if status == self.STATUS_WAITING:
            self._label_status.SetLabel("Waiting")
            self._label_status.SetForegroundColour(self.COLOR_DEFAULT)
        elif status == self.STATUS_IN_PROGRESS:
            self._label_status.SetLabel("In Progress")
            self._label_status.SetForegroundColour(self.COLOR_IN_PROGRESS)
        elif status == self.STATUS_COMPLETE:
            self._label_status.SetLabel("Complete")
            self._label_status.SetForegroundColour(self.COLOR_COMPLETE)
        elif status == self.STATUS_FAILED:
            self._label_status.SetLabel("Failed")
            self._label_status.SetForegroundColour(self.COLOR_FAILED)
        elif status == self.STATUS_DISABLED:
            self._label_status.SetLabel("Disabled")
            self._label_status.SetForegroundColour(self.COLOR_DISABLED)

    def set_texture_path(self, path):
        '''
        Sets the slot's Texture Path

        :param path: The path to use
        :type path: str
        '''
        self.fp_texture_path.SetPath(path)
        self.fp_texture_path.GetTextCtrl().SetInsertionPointEnd()

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

    # ============================================================================================================
    # Internal Methods
    # ============================================================================================================
    def _create_cell(self, widget, column, proportion):
        '''
        Create a slot cell and adds the provided widget to it
        
        :param widget: The widget to add to the cell
        :type widget: wx.Window
        :param column: The column to add the widget to
        :type column: wx.Sizer
        '''
        cell_sizer = self._build_cell_sizer()
        cell_sizer.Add(widget, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        column.Add(cell_sizer, proportion, wx.ALL | wx.EXPAND, 5)
        column.FitInside(self._table)
        self._cells.append(cell_sizer)

    def _build_cell_sizer(self):
        '''
        Builds a cell sizer to hold cell content, with correct alignment and size (vertically centered)

        :returns: The new sizer
        :rtype: wx.Sizer
        '''

        cell_sizer = wx.BoxSizer(wx.HORIZONTAL)
        cell_sizer.SetMinSize(self.MIN_CELL_SIZE)
        return cell_sizer
