# ============================================================================================================
# Imports: External
# ============================================================================================================
import os

# ============================================================================================================
# Imports: Internal
# ============================================================================================================
from textureforge.components.image_discovery import ImageDiscoverer
from textureforge.utils import utils
from test.abs_test_case import AbsTestCase

# ============================================================================================================
# Image Discoverer Test Case Class
# ============================================================================================================
class ImageDiscovererTestCase(AbsTestCase):
    '''
    Image Discoverer Test Case
    '''

    # ============================================================================================================
    # Methods
    # ============================================================================================================
    def setUp(self):
        '''
        DDS Processor TC set up
        '''
        self._id = ImageDiscoverer()
        super(ImageDiscovererTestCase, self).setUp()

    def tearDown(self):
        '''
        DDS Processor TC tear down
        '''
        super(ImageDiscovererTestCase, self).tearDown()

    # ============================================================================================================
    # Unit Tests
    # ============================================================================================================
    def test_image_discovery_png(self):
        '''
        Test Image discovery for a folder containing PNG files
        '''

        # Find Images
        image_files = self._id.search_directory(self.PATH_TEST_SAMPLES_PNG)

        # Check discovery results
        self.assertEqual(3, len(image_files))
        for file in image_files:
            self.assertTrue(file.endswith(".png"))
