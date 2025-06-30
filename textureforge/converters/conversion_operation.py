# ==============================================================================
# Imports: External
# ==============================================================================

# ==============================================================================
# Imports: Internal
# ==============================================================================


# ==============================================================================
# Conversion Operation Class
# ==============================================================================
class ConversionOperation:
    '''
    Texture Conversion Operation
    '''

    def __init__(self, in_path, out_path, compression):
        '''
        Constructor

        :param in_path: Path to the image file to convert
        :type in_path: str
        :param out_path: The path to write the converted file to
        :type out_path: str
        :param compression: The Compression type to use
        :type compression: str
        '''
        self._in_path = in_path
        self._out_path = out_path
        self._compression = compression


    # ==============================================================================
    # Getters
    # ==============================================================================
    def get_in_path(self):
        '''
        Gets the Input File path

        :return: The Input File Path
        :rtype: str
        '''
        return self._in_path

    def get_out_path(self):
        '''
        Gets the Output File path

        :return: The Output File Path
        :rtype: str
        '''
        return self._out_path

    def get_compression(self):
        '''
        Gets the compression type

        :return: The compression type
        :rtype: str
        '''
        return self._compression
