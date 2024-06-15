import unittest
from task6 import *

from io import StringIO
import sys



class TestPrintEvenIndexValues(unittest.TestCase):

    def test_GenerateBBSTArray(self):
        test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        bst = GenerateBBSTArray(test_array)
        bst.print_tree()


if __name__ == '__main__':
    unittest.main()

