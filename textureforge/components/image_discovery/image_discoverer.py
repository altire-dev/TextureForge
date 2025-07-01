# ============================================================================================================
# Imports: External
# ============================================================================================================
import os

# ============================================================================================================
# Imports: Internal
# ============================================================================================================
from textureforge.utils import utils

# ============================================================================================================
# Image Discoverer Class
# ============================================================================================================
class ImageDiscoverer:
    '''
    Image Discoverer. Searches a directory for image files
    '''


    # ============================================================================================================
    # Properties
    # ============================================================================================================
    FORMAT_PNG = "png"
    FORMAT_JPG = "jpg"
    FORMAT_TGA = "tga"
    FORMAT_TIF = "tif"
    FORMAT_BMP = "bmp"
    FORMATS = [
        FORMAT_PNG,
        FORMAT_JPG,
        FORMAT_TGA,
        FORMAT_TIF,
        FORMAT_BMP,
    ]

    # ============================================================================================================
    # Methods
    # ============================================================================================================
    def __init__(self):
        '''
        Constructor
        '''
        pass

    def search_directory(self, path):
        '''
        Searches the specified directory for image files

        :param path: The path to the directory to search
        :type path: str
        :returns: List of discovered images
        :rtype: list[str]
        '''
        image_files = []

        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            extension = utils.get_file_extension_from_path(file_path)
            if extension in self.FORMATS:
                image_files.append(file_path)

        return image_files

