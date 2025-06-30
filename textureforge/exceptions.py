# ===================================================================================================
# TextureForge Exceptions
# ===================================================================================================

# ===================================================================================================
# Base TextureForge Exception Class
# ===================================================================================================
class TextureForgeException(Exception):
    '''
    Base TextureForge Exception. To be used as base class for all TextureForge exception types
    '''

# ===================================================================================================
# Bad DDS Format Exception Class
# ===================================================================================================
class BadDDSFormat(TextureForgeException):
    '''
    To be raised when an invalid, unknown or unsupported DDS Format is specified
    '''

    def __init__(self, format):
        '''
        Constructor

        :param format: The bad format that was specified or encountered
        :type format: str
        '''
        super(BadDDSFormat, self).__init__(
            "Invalid, unknown or unsupported DDS Compression format specified: %s" % format
        )


# ===================================================================================================
# Image Processing Exception Class
# ===================================================================================================
class ImageProcessingException(TextureForgeException):
    '''
    Generic Image Processing error. Raised when an Image Processing error of some kind occurs
    '''

    def __init__(self, msg):
        '''
        Constructor

        :param msg: The error message to raise to the user/caller
        :type msg: str
        '''
        super(ImageProcessingException, self).__init__(msg)