# ===================================================================================================
# Imports: External
# ===================================================================================================
import os
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
    COMPRESSION_BC1 = "BC1_UNORM"
    COMPRESSION_BC2 = "BC2_UNORM"
    COMPRESSION_BC3 = "BC3_UNORM"
    COMPRESSION_BC4 = "BC4_UNORM"
    COMPRESSION_BC5 = "BC5_UNORM"
    COMPRESSION_BC7 = "BC7_UNORM"

    COMPRESSION_FORMATS = {
        COMPRESSION_BC1: {
            "cid": "BC1_UNORM",
            "display_name": "BC1 - No-Alpha (DXT1)"
        },
        COMPRESSION_BC2: {
            "cid": "BC2_UNORM",
            "display_name": "BC2 - Explicit Alpha (DXT3)"
        },
        COMPRESSION_BC3: {
            "cid": "BC3_UNORM",
            "display_name": "BC3 - Interpolated Alpha (DXT5)"
        },
        COMPRESSION_BC4: {
            "cid": "BC4_UNORM",
            "display_name": "BC4 - One Channel"
        },
        COMPRESSION_BC5: {
            "cid": "BC5_UNORM",
            "display_name": "BC5 - Two Channel"
        },
        COMPRESSION_BC7: {
            "cid": "BC7_UNORM",
            "display_name": "BC7 - HQ RGBA"
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

    def convert_to_dds(self, in_path, out_dir_path, compression=COMPRESSION_BC1, overwrite=True):
        '''
        Converts the specified image into a DDS image file

        :param in_path: The path to the image to convert
        :type in_path: str
        :param out_dir_path: The directory to write the converted DDS file to
        :type out_dir_path: str
        :param compression: The DDS Compression format to use. Defaults to BC1 (No Alpha)
        :type compression: str
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
        if not self.is_valid_compression_type(compression):
            raise BadDDSFormat(compression)

        # ============================================================================================================
        # Build TexConv Command
        # ============================================================================================================
        cmd = [utils.get_texconv_path()]
        cmd += ["-o", out_dir_path]
        if overwrite:
            cmd.append("-y")
        cmd += ["-f", self.COMPRESSION_FORMATS[compression]["cid"]]
        cmd.append(in_path)
        print("Running command: %s" % " ".join((cmd)))


        # ============================================================================================================
        # Run TexConv Process
        # ============================================================================================================
        process = Popen(
            cmd,
            stdout=PIPE
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
            "compression": None
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
            stdout=PIPE
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
                compression = line.split(" = ")[1]
                info["compression"] = compression
                continue

        return info

    def get_image_compression(self, path):
        '''
        Gets the compression of the DDS Image at the specified path

        :param path: The path of the target DDS image file
        :type path: str
        :returns: Compression type used by the specified image file
        :rtype: str
        '''
        image_info = self.get_image_info(path)
        return image_info["compression"]

    def is_valid_compression_type(self, compression):
        '''
        Checks the that specified compression is a known, valid and supported DDS compression format

        :param compression: The compression format to check
        :type compression: str
        '''
        return compression.upper() in self.COMPRESSION_FORMATS

    # ============================================================================================================
    # Getters
    # ============================================================================================================

