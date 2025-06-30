# ============================================================================================================
# Imports: External
# ============================================================================================================
import os
from unittest import TestCase

# ============================================================================================================
# Imports: Internal
# ============================================================================================================


# ============================================================================================================
# Base Test Case Class
# ============================================================================================================
class AbsTestCase(TestCase):
    '''
    Base Test Case Class. Not to be instantiated directly
    '''

    # ============================================================================================================
    # Properties
    # ============================================================================================================
    PATH_TEST_DATA                  = os.path.join(os.path.dirname(__file__), "data")
    PATH_TEST_TMP                   = os.path.join(PATH_TEST_DATA, "tmp")
    PATH_TEST_SAMPLES               = os.path.join(PATH_TEST_DATA, "samples")

    PATH_TEST_SAMPLES_PNG           = os.path.join(PATH_TEST_SAMPLES, "png")
    PATH_TEST_SAMPLES_PNG_DIFFUSE   = os.path.join(PATH_TEST_SAMPLES_PNG, "sample_diffuse.png")
    PATH_TEST_SAMPLES_PNG_METALLIC  = os.path.join(PATH_TEST_SAMPLES_PNG, "sample_metallic.png")
    PATH_TEST_SAMPLES_PNG_NORMAL    = os.path.join(PATH_TEST_SAMPLES_PNG, "sample_normal.png")

    PATH_TEST_SAMPLES_DDS           = os.path.join(PATH_TEST_SAMPLES, "dds")
    PATH_TEST_SAMPLES_DDS_DIFFUSE   = os.path.join(PATH_TEST_SAMPLES_DDS, "sample_diffuse.dds")
    PATH_TEST_SAMPLES_DDS_METALLIC  = os.path.join(PATH_TEST_SAMPLES_DDS, "sample_metallic.dds")
    PATH_TEST_SAMPLES_DDS_NORMAL    = os.path.join(PATH_TEST_SAMPLES_DDS, "sample_normal.dds")


    # ============================================================================================================
    # Methods
    # ============================================================================================================
    def setUp(self):
        '''
        Test Case Set Up
        '''
        super(AbsTestCase, self).setUp()

    def tearDown(self):
        '''
        Test Case Tear Down
        '''
        super(AbsTestCase, self).tearDown()


    # ============================================================================================================
    # Custom Assertions
    # ============================================================================================================


