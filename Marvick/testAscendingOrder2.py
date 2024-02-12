import unittest
import AscendingOrder2

class TestAscendingOrder(unittest.TestCase):
    def test_Ascending_Order2_is_not_none(self):
        self.assertIsNotNone(AscendingOrder2.Ascending_Order2)
    def test_Ascending_Order2(self):
        Sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        Sample_output = [1, 2, 3, 4, 5, 8, 9, 10]
        self.assertEqual(AscendingOrder2.Ascending_Order2(Sample_list), Sample_output)  # add assertion here

class TestDescendingOrder(unittest.TestCase):
    def test_Descending_Order2_is_not_none(self):
        self.assertIsNotNone(AscendingOrder2.Descending_Order2)
    def test_Descending_Order2(self):
        Sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        Sample_output = [10, 9, 8, 5, 4, 3, 2, 1]
        self.assertEqual(AscendingOrder2.Descending_Order2(Sample_list), Sample_output)  # add assertion here

class TestThatKeyIsPresentFunction(unittest.TestCase):
    def test_that_function_is_not_none(self):
        self.assertIsNotNone(AscendingOrder2.Search_key)


    def test_that_key_exist_return_index(self):
        Sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        self.assertEqual(2, AscendingOrder2.Search_key(Sample_list, 7))
        self.assertEqual(4, AscendingOrder2.Search_key(Sample_list, 3))
        self.assertEqual(9, AscendingOrder2.Search_key(Sample_list, 5))
