import unittest
from unittest import TestCase

from Marvick.MethodString import MethodString


class MyTestCase(unittest.TestCase):
    def test_for_name(self):
        myMethodString = MethodString()
        myMethodString.name_input("okay")
        self.assertEqual("timi", myMethodString.printString())
