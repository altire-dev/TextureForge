# ================================================================================
# Imports: External
# ================================================================================
from threading import Thread
from threading import Event

# ================================================================================
 # Imports: Internal
 # ================================================================================

# ================================================================================
# Texture Converter: Base Class for all Texture Converters
# ================================================================================
class TextureConverter(Thread):
    '''
    Base Texture Converter. DO NOT instantiate directly
    '''

    # ================================================================================
    # Properties
    # ================================================================================

    # ================================================================================
    # Methods
    # ================================================================================
    def __init__(self):
        '''
        Constructor
        '''
        self._stop_event = Event()

        super(TextureConverter, self).__init__()


    def start_conversion(self):
        '''
        Starts the conversion process
        '''
        self.start()

    def stop(self):
        '''
        Starts the conversion process
        '''
        self._stop_event.set()

    def run(self):
        '''
        Texture Converter: Run method. MUST be overriden
        :raises: NotImplementedError
        '''
        raise NotImplementedError("Run method must be implemented on derived classes")

