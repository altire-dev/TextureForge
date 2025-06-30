# ==============================================================================
# Imports: External
# ==============================================================================
import time
from PIL import Image

# ==============================================================================
# Imports: Internal
# ==============================================================================
from ..texture_converter import TextureConverter
from ...processors import DDSProcessor

# ==============================================================================
# DDS Converter Class
# ==============================================================================
class DDSConverter(TextureConverter):
    '''
    DDS Converter. Converts image textures to DDS format
    '''


    # ==============================================================================
    # Properties
    # ==============================================================================

    # ==============================================================================
    # Methods
    # ==============================================================================
    def __init__(self, tfgui, output_dir, target_maps):
        '''
        Constructor

        :param tfgui: The parent TextureForge GUI instance
        :type tfgui: TextureForgeGUI
        :param output_dir: Path to the output directory
        :type output_dir: str
        :param target_maps: List of Maps to convert
        :type target_maps: list[tuple]
        '''
        self._tfgui = tfgui
        self._output_dir = output_dir
        self._target_maps = target_maps
        super(DDSConverter, self).__init__()

    def run(self):
        '''
        Converts the PNG file at the specified path into a DDS file with the specified compressions
        '''
        print("Performing %s conversion operations" % len(self._target_maps))
        dds_processor = DDSProcessor()

        for map in self._target_maps:
            path, compression, slot = map[0], map[1], map[2]
            slot.set_status(slot.STATUS_IN_PROGRESS)

            print("Converting image file: %s --> %s (%s)" % (path, self._output_dir, compression))
            dds_processor.convert_to_dds(path, self._output_dir, compression)
            slot.set_status(slot.STATUS_COMPLETE)
            self._tfgui.on_map_converted(slot)


        self._tfgui.on_conversion_finished()








