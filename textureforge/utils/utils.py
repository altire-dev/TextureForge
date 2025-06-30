# ============================================================================================================
# General Utilities
# ============================================================================================================

# ============================================================================================================
# Imports: External
# ============================================================================================================
import os

# ============================================================================================================
# Imports: Internal
# ============================================================================================================

# ============================================================================================================
# Utilities: General Helper functions
# ============================================================================================================
def get_texconv_path():
    '''
    Gets the path to the TexConv executable

    :returns: Path to the TexConv executable
    :rtype: str
    '''
    return os.path.join(get_bin_path(), "texconv.exe")

def get_texdiag_path():
    '''
    Gets the path to the TexDiag executable

    :returns: Path to the TexDiag executable
    :rtype: str
    '''
    return os.path.join(get_bin_path(), "texdiag.exe")

def get_bin_path():
    '''
    Gets the path to the TextureForge bin directory

    :returns: Path to the TextureForge "bin" directory
    :rtype: str
    '''
    return os.path.join(get_tf_root_path(), "bin")

def get_tf_root_path():
    '''
    Gets the path to the TextureForge root directory
    '''
    utils_path = os.path.dirname(__file__)
    return os.path.dirname(utils_path)

def get_path_filename(path):
    '''
    Extracts the filename from a path

    :param path: The path to extract the filename from
    :type path: str
    :returns: The extract filename, or None if the last path element is NOT a file
    :rtype: str, None
    '''
    if not os.path.isfile(path):
        return None
    return os.path.split(path)[1]

def get_file_extension_from_path(path):
    '''
    Gets the file extension of the file at the specified path

    :param path: Path to the target file
    :type path: str
    :returns: The file's extension, or None if the path does not point to a file, or the file has no extension
    '''
    extension = None
    filename = get_path_filename(path)
    if filename:
        if filename.split(".") > 1:
            extension.split(".")[-1]
    return extension




# ============================================================================================================
# Test Bed
# ============================================================================================================
if __name__ == "__main__":
    print("TF Root Path: %s" % get_tf_root_path())
    print("TexConv Path: %s" % get_texconv_path())
