import unittest
from Marvick import display_single_string

class test_for_two_string(unittest.TestCase):
    def test_enter_two_strings(self):

        sample1 = 'abcd'
        sample2 = 'vxyz'
        sample_output = 'vxcd abyz'
        self.assertEqual(sample_output, display_single_string.enter_two_strings(sample1,sample2) )
