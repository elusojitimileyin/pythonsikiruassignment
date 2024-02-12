import unittest

from Marvick import task_one


class Test(unittest.TestCase):

    def test_get_length_of_list(self):
        my_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert task_one.get_length_of_list(my_lists) == 10

    def test_get_sum_of_even_list(self):
        my_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert task_one.get_sum_of_the_even_position_on_the_list(my_lists) == 30

    def test_get_sum_of_odd_list(self):
        my_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert task_one.get_sum_of_the_odd_position_on_the_list(my_lists) == 25

    def test_get_multiply_of_the_third_position_on_the_list(self):
        my_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert task_one.get_multiply_of_the_thrid_position_of_the_list(my_lists) == 162




