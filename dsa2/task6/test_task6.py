import unittest
from task6 import *

from io import StringIO
import sys


class TestPrintEvenIndexValues(unittest.TestCase):

    def test_one_zero_element(self):
        test_array = [0]
        bst = GenerateBBSTArray(test_array)
        bst.print_tree()

    def test_one_element(self):
        test_array = [1]
        bst = GenerateBBSTArray(test_array)
        bst.print_tree()

    def test_two_elements(self):
        test_array = [1, 2]
        bst = GenerateBBSTArray(test_array)
        bst.print_tree()

    def test_same_elements(self):
        test_array = [1, 2, 1, 1, 2, 1, 1]
        bst = GenerateBBSTArray(test_array)
        bst.print_tree()

    def test_GenerateBBSTArray(self):
        test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        bst = GenerateBBSTArray(test_array)
        bst.print_tree()

    def test_error(self):
        unsorted_array = [7, 4, 9, 1, 6, 8, 10]

        # Примерная структура кода, который может вызвать зацикливание:
        bst = BST(None)
        add_middle_to_bst(unsorted_array, bst)


if __name__ == '__main__':
    unittest.main()
