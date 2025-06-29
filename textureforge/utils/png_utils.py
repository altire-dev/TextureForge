# ===================================================================================================
# Imports: External
# ===================================================================================================
import os
import sys
from PIL import Image

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
def jpg_to_png_folder_convert(path):
    '''
    Converts all JPG Files in the specified folder into PNGs

    :param path: Path to the folder of JPG files to convert
    :type path: str
    '''
    count = 0

    output_dir = os.path.join(path, "png")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(path):
        abs_path = os.path.join(path, file).lower()
        if not os.path.isfile(abs_path) or not abs_path.endswith(".jpg"):
            print("Skipping invalid file: %s" % abs_path)
            continue

        in_file_name = os.path.split(abs_path)[-1]
        out_file_name = in_file_name.replace(".jpg", ".png")
        output_path = os.path.join(output_dir, out_file_name)

        print("[+] Converting %s to %s" % (in_file_name, out_file_name))
        jpg_image = Image.open(abs_path)
        jpg_image.save(output_path)
        count += 1

    print("[!] CONVERSION COMPLETE [!!]")
    print("%s JPG file(s) converted to PNG" % count)


# ===================================================================================================
# ENTRY
# ===================================================================================================
if __name__ == "__main__":

    # ===================================================================================================
    # Validate Directory
    # ===================================================================================================
    if len(sys.argv) <= 1:
        raise RuntimeError("Directory must be specified")
    dir_to_convert = sys.argv[1]

    if not os.path.isdir(dir_to_convert):
        raise RuntimeError("Specified path does not exist, or is not a valid directory")

    jpg_to_png_folder_convert(dir_to_convert)
