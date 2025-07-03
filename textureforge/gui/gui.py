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
from .tabs import TFTabDDSConverter
from ..utils import utils
from .abs_gui import TextureForgeMF

# ============================================================================================================
# DPI Fix
# ============================================================================================================
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

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
        self._tabs = []

        # Initialise Frame
        super(TextureForgeGUI, self).__init__(None)

        # Set up GUI
        self._init_ui()
        self._bind_events()


    def _bind_events(self):
        '''
        Binds UI Events
        '''

        self.Bind(wx.EVT_CLOSE, self._on_close)


    def _init_ui(self):
        '''
        Initialses the UI, updating and overriding any properties
        '''

        # ============================================================================================================
        # Update Main Frame
        # ============================================================================================================
        self.SetTitle(self.get_base_title())
        if not self.GetParent():
            icon = wx.Icon()
            icon.CopyFromBitmap(wx.Bitmap(self._get_icon_path()))
            self.SetIcon(icon)

        # ============================================================================================================
        # Initialise Tabs
        # ============================================================================================================
        # Tab: DDS Converter
        tab_dds_converter = TFTabDDSConverter(self, self.Notebook)
        self._tabs.append(tab_dds_converter)
        self.Notebook.AddPage(tab_dds_converter, "DDS Converter")


    # ===================================================================================================
    # Getters
    # ===================================================================================================
    def get_base_title(self):
        '''
        Gets the application's base title

        :returns: The application's base title
        :rtype: str
        '''
        return "TextureForge v%s" % self._version


    # ===================================================================================================
    # Setters
    # ===================================================================================================
    def set_title_context(self, context):
        '''
        Sets the application's title context

        :param context: The context string to use
        :type context: str
        '''
        self.SetTitle(self.get_base_title() + " - " + context)


    # ===================================================================================================
    # Event Handlers
    # ===================================================================================================
    def _on_close(self, event):
        '''
        Handler: application closed

        :param event: The wx Close event
        :type event: wx.Event
        '''

        # Makes tabs aware of closure
        for tab in self._tabs:
            tab.on_close()

        self.Destroy()


    # ============================================================================================================
    # Internal Methods
    # ============================================================================================================
    def _get_icon_path(self):
        '''
        Gets the path to the GUI Icon (.ico) file

        :return: The path to the GUI Icon File
        :rtype: str
        '''
        tf_root = utils.get_tf_root_path()

        # Packed EXE
        if "_MEI" in __file__:
            base_path = os.path.join(os.path.dirname(tf_root), "resources")
        # Script
        else:
            base_path = os.path.join(tf_root, "resources")

        icon_path = os.path.join(base_path, "icon.ico")
        return icon_path






