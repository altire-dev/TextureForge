# ===================================================================================================
# Imports: External
# ===================================================================================================
import wx
from wx._core import wxAssertionError

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
from .gui import TextureForgeGUI


# ===================================================================================================
# Properties
# ===================================================================================================
VERSION = "1.0.0"
AUTHOR = "Altire"

# ===================================================================================================
# Texture Force Class
# ===================================================================================================
class TextureForge():
    '''
    Texture Forge. Main object for the Texture Forge Package
    '''

    def __init__(self):
        '''
        Constructor
        '''

        # Initialise GUI
        self._app = wx.App()
        self._gui = TextureForgeGUI(VERSION, AUTHOR)


    def launch(self):
        '''
        Launches the Texture Forge GUI
        '''

        self._gui.Show()

        # Ignore wx Assertion Failures
        try:
            self._app.MainLoop()
        except wxAssertionError as ex:
            print("WX Assertion error (likely during app close): %s" % ex)
