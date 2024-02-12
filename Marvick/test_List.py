import unittest
import pytest
import task_one_solution


class TestListFunction(unittest ):

    def test_get_length_of_list(self):
        my_lists = list(range(10, 20))
        assert taskonesolution.get_length_of_list(my_lists) == 10

    def test_get_sum_of_even_list(self):
        my_lists = list(range(10, 20))
        assert taskonesolution.get_sum_of_the_even_position_on_the_list(my_lists) == 75

    def test_get_sum_of_odd_list(self):
        my_lists = list(range(10, 20))
        assert taskonesolution.get_sum_of_the_odd_position_on_the_list(my_lists) == 70

    # def test_get_product_of_third_element(self):
    #     my_lists = list(range(10, 20))
    #     assert taskonesolution.get_product_of_third_element(my_lists) == 3240

    def test_get_average(self):
        my_lists = list(range(10, 20))
        assert taskonesolution.get_average(my_lists) == 14.5

    def test_get_largest(self):
        my_lists = list(range(10, 20))
        assert taskonesolution.get_largest(my_lists) == 19

    def test_get_minium(self):
        my_lists = list(range(10, 20))
        assert taskonesolution.get_minium(my_lists) == 10

    def test_that_function_return_list_of_strings(self):
        my_lists = ["hannah", "praise", "vicky", "balikis", "bolaji"]
        assert taskonesolution.get_string(my_lists) == ["hannah"]

        my_lists2 = ["hannah", "femi", "vicky", "balikis", "bolaji"]
        assert taskonesolution.get_string(my_lists) == ["hannah"]
