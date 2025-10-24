# ===================================================================================================
# Affinity Suite Utilities
# ===================================================================================================

# ===================================================================================================
# Imports: External
# ===================================================================================================
import os
import subprocess
from subprocess import Popen, PIPE

# ===================================================================================================
# Utility Methods
# ===================================================================================================
def open_image(app_path, file_path):
    '''
    Opens the image file using the specified Affinity application executable

    :param afd_path: Path to relevant Affinity 2 executable
    :type afd_path: str
    :param file_path: Path of the file to open
    :type file_path: str
    '''

    # Build Command
    cmd = [app_path, file_path]
    print("Running command %s" % cmd)

    process = Popen(cmd, stdout=PIPE, creationflags=subprocess.CREATE_NO_WINDOW)

def get_designer_path():
    '''
    Attempts to find and locate the path to the Affinity Designer 2 executable

    :returns: Path to Affinity Designer 2 executable, or None if executable could not be found
    :rtype: str, None
    '''
    path = None
    appdata_path = os.getenv("LOCALAPPDATA")

    winapps_path = os.path.join(appdata_path, "Microsoft", "WindowsApps")
    winapps_content = os.listdir(winapps_path)

    if "AffinityDesigner2.exe" in winapps_content:
        path = os.path.join(winapps_path, "AffinityDesigner2.exe")

    return path

def get_photo_path():
    '''
    Attempts to find and locate the path to the Affinity Photo 2 executable

    :returns: Path to Affinity Photo 2 executable, or None if executable could not be found
    :rtype: str, None
    '''
    path = None
    appdata_path = os.getenv("LOCALAPPDATA")

    winapps_path = os.path.join(appdata_path, "Microsoft", "WindowsApps")
    winapps_content = os.listdir(winapps_path)

    if "AffinityPhoto2.exe" in winapps_content:
        path = os.path.join(winapps_path, "AffinityPhoto2.exe")

    return path
