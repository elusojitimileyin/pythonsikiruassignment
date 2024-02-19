from unittest import TestCase

from Marvick.MethodString import MethodString


class test_MethodString(TestCase):
    def test_for_name(self):
        myMethodString = MethodString()
        myMethodString.name_inputs("okay")
        self.assertEqual("OKAY", myMethodString.printString())


