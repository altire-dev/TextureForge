# ============================================================================================================
# General Utilities
# ============================================================================================================
import datetime
# ============================================================================================================
# Imports: External
# ============================================================================================================
import os
import subprocess

# ============================================================================================================
# Imports: Internal
# ============================================================================================================

# ============================================================================================================
# Utilities: General Helper functions
# ============================================================================================================
def open_explorer(path):
    '''
    Opens Windows Explorer at the specified path

    :param path: The target path
    :type path: str
    '''
    cmd = 'explorer "%s"' % path
    subprocess.Popen(cmd)

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
    tf_root = get_tf_root_path()
    base_dir = tf_root

    if "_MEI" in __file__:  # (Packed)
        base_dir = os.path.dirname(tf_root)

    return os.path.join(base_dir, "bin")

def get_tf_root_path():
    '''
    Gets the path to the TextureForge root directory
    '''
    utils_path = os.path.dirname(__file__)
    return os.path.dirname(utils_path)

def get_path_filename(path, exclude_extension=False):
    '''
    Extracts the filename from a path

    :param path: The path to extract the filename from
    :type path: str
    :param exclude_extension: Whether the file extension should be stripped. Defaults to False
    :type exclude_extension: bool, Optional
    :returns: The extracted filename, or None if the last path element is NOT a file
    :rtype: str, None
    '''
    filename = None
    if len(os.path.split(path)) > 1:
        filename = os.path.split(path)[1]
        if exclude_extension:
            filename = filename.split(".")[0]

    return filename

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
        if len(filename.split(".")) > 1:
            extension = filename.split(".")[-1].lower()
    return extension


def get_datetime_string():
    '''
    Gets the datetime string for now

    :return: The datetime string for now
    :rtype: str
    '''
    now = datetime.datetime.now()
    dt_string = datetime.datetime.strftime(now, "%H:%M:%S")
    return dt_string


# ============================================================================================================
# Test Bed
# ============================================================================================================
if __name__ == "__main__":
    print(get_datetime_string())
