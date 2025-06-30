# ============================================================================================================
# Imports: External
# ============================================================================================================
import os

# ============================================================================================================
# Imports: Internal
# ============================================================================================================
from textureforge.processors import DDSProcessor
from textureforge.utils import utils
from test.abs_test_case import AbsTestCase

# ============================================================================================================
# DDS Processor Test Case Class
# ============================================================================================================
class DDSProcessorTestCase(AbsTestCase):
    '''
    DDS Processor Test Case
    '''

    # ============================================================================================================
    # Methods
    # ============================================================================================================
    def setUp(self):
        '''
        DDS Processor TC set up
        '''
        self._p = DDSProcessor()
        super(DDSProcessorTestCase, self).setUp()

    def tearDown(self):
        '''
        DDS Processor TC tear down
        '''
        super(DDSProcessorTestCase, self).tearDown()


    # ============================================================================================================
    # Unit Tests
    # ============================================================================================================
    def test_dds_conversion_bc1(self):
        '''
        Test Test (lol)
        '''
        print(self.PATH_TEST_SAMPLES_PNG_DIFFUSE)

        # Attempt Conversion
        result = self._p.convert_to_dds(
            self.PATH_TEST_SAMPLES_PNG_DIFFUSE,
            self.PATH_TEST_TMP
        )

        print("RC: %s" % result["status_code"])
        print("Output: %s" % result["output"])
        print("Error: %s" % result["error"])

        # Check Image
        self.assertTrue(result["success"])
        self.assertEqual(self._p.COMPRESSION_BC1, self._p.get_image_compression(result["out_path"]))

    def test_dds_conversion_bc2(self):
        '''
        Test Test (lol)
        '''
        print(self.PATH_TEST_SAMPLES_PNG_DIFFUSE)

        # Attempt Conversion
        result = self._p.convert_to_dds(
            self.PATH_TEST_SAMPLES_PNG_DIFFUSE,
            self.PATH_TEST_TMP,
            DDSProcessor.COMPRESSION_BC2
        )

        print("RC: %s" % result["status_code"])
        print("Output: %s" % result["output"])
        print("Error: %s" % result["error"])

        # Check status
        self.assertTrue(result["success"])
        self.assertEqual(self._p.COMPRESSION_BC2, self._p.get_image_compression(result["out_path"]))

    def test_get_image_info(self):
        '''
        Tests that we can get the image information for a DDS image file
        '''

        info = self._p.get_image_info(self.PATH_TEST_SAMPLES_DDS_DIFFUSE)
        self.assertEqual(info["width"], "2048")
        self.assertEqual(info["height"], "2048")
        self.assertEqual(info["compression"], self._p.COMPRESSION_BC3)





