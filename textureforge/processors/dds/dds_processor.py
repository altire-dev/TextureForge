# ===================================================================================================
# Imports: External
# ===================================================================================================
import os
import subprocess
from subprocess import Popen
from subprocess import PIPE

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
from ...utils import utils
from ...exceptions import *
from ..processor import TFImageProcessor

# ===================================================================================================
# TextureForge DDS Image Processor Class
# ===================================================================================================
class DDSProcessor(TFImageProcessor):
    '''
    TextureForge DDS Image Processor
    '''

    # ===================================================================================================
    # Properties
    # ===================================================================================================

    # ===================================================================================================
    #  Format Names
    # ===================================================================================================
    FORMAT_BC1          = "BC1_UNORM"
    FORMAT_BC1_SRGB     = "BC1_UNORM_SRGB"

    FORMAT_BC2          = "BC2_UNORM"
    FORMAT_BC2_SRGB     = "BC2_UNORM_SRGB"

    FORMAT_BC3          = "BC3_UNORM"
    FORMAT_BC3_SRGB     = "BC3_UNORM_SRGB"

    FORMAT_BC4          = "BC4_UNORM"
    FORMAT_BC4S         = "BC4_SNORM"

    FORMAT_BC5          = "BC5_UNORM"
    FORMAT_BC5S         = "BC5_SNORM"

    FORMAT_BC6          = "BC6H_UF16"
    FORMAT_BC6S         = "BC6H_SF16"

    FORMAT_BC7          = "BC7_UNORM"
    FORMAT_BC7_SRGB     = "BC7_UNORM_SRGB"

    FORMAT_RGBA8            = "R8G8B8A8_UNORM"
    FORMAT_RGBA8S           = "R8G8B8A8_SNORM"
    FORMAT_RGBA8_SRGB        = "R8G8B8A8_UNORM_SRGB"

    FORMAT_R8U              = "R8_UNORM"
    FORMAT_R16U             = "R16_UNORM"

    FORMAT_R32_FLOAT        = "R32_FLOAT"


    # ===================================================================================================
    # Format Schema
    # ===================================================================================================
    FORMATS = {
        FORMAT_BC1: {
            "cid": FORMAT_BC1,
            "display_name": "BC1 - No-Alpha (DXT1)",
            "compressed": True
        },
        FORMAT_BC1_SRGB: {
            "cid": FORMAT_BC1_SRGB,
            "display_name": "BC1 (SRGB) - No-Alpha (DXT1)",
            "compressed": True
        },
        FORMAT_BC2: {
            "cid": FORMAT_BC2,
            "display_name": "BC2 - Explicit Alpha (DXT3)",
            "compressed": True
        },
        FORMAT_BC2_SRGB: {
            "cid": FORMAT_BC2_SRGB,
            "display_name": "BC2 - (SRGB) Explicit Alpha (DXT3)",
            "compressed": True
        },
        FORMAT_BC3: {
            "cid": FORMAT_BC3,
            "display_name": "BC3 - Interpolated Alpha (DXT5)",
            "compressed": True
        },
        FORMAT_BC3_SRGB: {
            "cid": FORMAT_BC3_SRGB,
            "display_name": "BC3 - (SRGB) Interpolated Alpha (DXT5)",
            "compressed": True
        },
        FORMAT_BC4: {
            "cid": FORMAT_BC4,
            "display_name": "BC4 - Grayscale",
            "compressed": True
        },
        FORMAT_BC4S: {
            "cid": FORMAT_BC4S,
            "display_name": "BC4 - (Signed) Grayscale",
            "compressed": True
        },
        FORMAT_BC5: {
            "cid": FORMAT_BC5,
            "display_name": "BC5 - Two Channel",
            "compressed": True
        },
        FORMAT_BC5S: {
            "cid": FORMAT_BC5S,
            "display_name": "BC5 - (Signed) Two Channel",
            "compressed": True
        },
        FORMAT_BC6: {
            "cid": FORMAT_BC6,
            "display_name": "BC6 - HDR",
            "compressed": True
        },
        FORMAT_BC6S: {
            "cid": FORMAT_BC6S,
            "display_name": "BC6 - (Signed) HDR",
            "compressed": True
        },
        FORMAT_BC7: {
            "cid": FORMAT_BC7,
            "display_name": "BC7",
            "compressed": True
        },
        FORMAT_BC7_SRGB: {
            "cid": FORMAT_BC7_SRGB,
            "display_name": "BC7 (SRGB)",
            "compressed": True
        },
        FORMAT_RGBA8: {
            "cid": FORMAT_RGBA8,
            "display_name": "Uncompressed - RGBA8",
            "compressed": False
        },
        FORMAT_RGBA8S: {
            "cid": FORMAT_RGBA8S,
            "display_name": "Uncompressed - RGBA8 (Signed)",
            "compressed": False
        },
        FORMAT_RGBA8_SRGB: {
            "cid": FORMAT_RGBA8_SRGB,
            "display_name": "Uncompressed - RGBA8 SRGB (Signed)",
            "compressed": False
        },
        FORMAT_R8U: {
            "cid": FORMAT_R8U,
            "display_name": "Uncompressed - R8",
            "compressed": False
        },
        FORMAT_R16U: {
            "cid": FORMAT_R16U,
            "display_name": "Uncompressed - R16",
            "compressed": False
        },
        FORMAT_R32_FLOAT: {
            "cid": FORMAT_R32_FLOAT,
            "display_name": "Uncompressed - R32 Float",
            "compressed": False
        },
    }

    # ===================================================================================================
    # Methods
    # ===================================================================================================
    def __init__(self):
        '''
        Constructor
        '''
        pass
        self._tc_path = utils.get_texconv_path()

    def convert_to_dds(self, in_path, out_dir_path, format=FORMAT_BC1, overwrite=True):
        '''
        Converts the specified image into a DDS image file

        :param in_path: The path to the image to convert
        :type in_path: str
        :param out_dir_path: The directory to write the converted DDS file to
        :type out_dir_path: str
        :param format: The DDS file format to use. Defaults to compressed - BC1 (No Alpha)
        :type format: str
        :param overwrite: Overwrite output file, if it already exists. Defaults to True
        :type overwrite: bool, Optional
        :returns: Results of the conversion process
        :rtype: dict
        '''
        result = {
            "success": True,
            "status_code": 0,
            "output": None,
            "error": None,
            "outpath": None
        }

        # ===================================================================================================
        # Run Validation
        # ===================================================================================================
        if not self.is_valid_format_type(format):
            raise BadDDSFormat(format)

        # ============================================================================================================
        # Build TexConv Command
        # ============================================================================================================
        cmd = [utils.get_texconv_path()]
        cmd += ["-o", out_dir_path]
        if overwrite:
            cmd.append("-y")
        cmd += ["-f", self.FORMATS[format]["cid"]]
        cmd.append(in_path)
        print("Running command: %s" % " ".join((cmd)))


        # ============================================================================================================
        # Run TexConv Process
        # ============================================================================================================
        process = Popen(
            cmd,
            stdout=PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        stdout, stderr = process.communicate()
        result["output"] = stdout.decode("utf-8")
        result["status_code"] = process.returncode

        # ============================================================================================================
        # Process any Errors
        # ============================================================================================================
        if result["status_code"] != 0:
            result["success"] = False
            for line in result["output"].split("\r\n"):
                if line.startswith("ERROR:"):
                    result["error"] = line.strip("\r\n")

        out_file = utils.get_path_filename(in_path).replace(".png", ".dds")
        result["out_path"] = os.path.join(out_dir_path, out_file)

        return result

    def convert_to_tif(self, in_path, out_dir_path, overwrite=True):
        '''
        Converts a DDS image to a TIF

        :param in_path: The path to the DDS image to convert
        :type in_path: str
        :param out_dir_path: The directory to write the converted TIF file to
        :type out_dir_path: str
        :param overwrite: Overwrite output file, if it already exists. Defaults to True
        :type overwrite: bool, Optional
        :returns: Results of the conversion process
        :rtype: dict
        '''
        result = {
            "success": True,
            "status_code": 0,
            "output": None,
            "error": None,
            "outpath": None
        }

        # ===================================================================================================
        # Run Validation
        # ===================================================================================================
        # TODO

        # ============================================================================================================
        # Build TexConv Command
        # ============================================================================================================
        cmd = [utils.get_texconv_path()]
        cmd += ["-ft", "tif"]
        cmd += [ "-m", "1"]
        cmd += ["-o", out_dir_path]
        if overwrite:
            cmd.append("-y")
        cmd.append(in_path)
        print("Running command: %s" % " ".join(cmd))


        # ============================================================================================================
        # Run TexConv Process
        # ============================================================================================================
        process = Popen(
            cmd,
            stdout=PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        stdout, stderr = process.communicate()
        result["output"] = stdout.decode("utf-8")
        result["status_code"] = process.returncode

        # ============================================================================================================
        # Process any Errors
        # ============================================================================================================
        if result["status_code"] != 0:
            result["success"] = False
            for line in result["output"].split("\r\n"):
                if line.startswith("ERROR:"):
                    result["error"] = line.strip("\r\n")

        out_file = utils.get_path_filename(in_path).replace(".dds", ".tif")
        result["out_path"] = os.path.join(out_dir_path, out_file)
        print(result)

        return result



    def get_image_info(self, path):
        '''
        Gets the image information for the image at the specified path

        :param path: Path to the target image file
        :type path: str
        :returns: Image information for the specified image
        :rtype: ???
        '''
        info = {
            "width": None,
            "height": None,
            "format": None,
            "srgb_assumed": False,
        }

        # ============================================================================================================
        # Build TexDiag Command
        # ============================================================================================================
        cmd = [utils.get_texdiag_path(), "info"]
        cmd.append(path)
        print("Running command: %s" % " ".join((cmd)))

        # ============================================================================================================
        # Run TexConv Process
        # ============================================================================================================
        process = Popen(
            cmd,
            stdout=PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        stdout, stderr = process.communicate()
        output = stdout.decode("utf-8")

        # ============================================================================================================
        # Process any Errors
        # ============================================================================================================
        if process.returncode != 0:
            for line in output.split("\r\n"):
                if "ERROR:" in line or "FAILED" in line:
                    raise ImageProcessingException(line)

        # ===================================================================================================
        # Process Info Output
        # ===================================================================================================
        for line in output.split("\r\n"):
            if "width" in line:
                info["width"] = line.split(" = ")[1]
                continue
            if "height" in line:
                info["height"] = line.split(" = ")[1]
                continue
            if "format" in line:
                format = line.split(" = ")[1]

                # Check if SRGB should be assumed
                if format.split("_")[0] in ["BC1", "BC2", "BC3", "BC7"] and not format.endswith("SRGB"):
                    format += "_SRGB"
                    info["srgb_assumed"] = True
                info["format"] = format
                continue

        return info

    def get_image_format(self, path):
        '''
        Gets the format of the DDS Image at the specified path

        :param path: The path of the target DDS image file
        :type path: str
        :returns: Format used by the specified image file
        :rtype: str
        '''
        image_info = self.get_image_info(path)
        return image_info["format"]

    def is_valid_format_type(self, format):
        '''
        Checks the that specified format is a known, valid and supported DDS format

        :param format: The compression format to check
        :type format: str
        '''
        return format.upper() in self.FORMATS

    # ============================================================================================================
    # Getters
    # ============================================================================================================


