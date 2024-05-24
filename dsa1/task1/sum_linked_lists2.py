from io import StringIO

from task1 import Node, LinkedList
from typing import List, TextIO
import sys
import unittest


def sum_linked_lists2(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    The function takes two linked lists and if their lengths are equal,
    returns a new list where each element is the sum of corresponding elements from the input lists.
    Function returns the result list.
    All error messages are printed out in the stderr.
    """

    f: TextIO = sys.stderr
    ll_res = LinkedList()

    if ll1 is None or ll2 is None:
        print("Bad data.", file=f)
        return ll_res

    l1: int = ll1.len()
    l2: int = ll2.len()

    if l1 != l2:
        print("Lengths of lists are not equal.", file=f)
        return ll_res

    if l1 == 0:
        print("Lists are empty.", file=f)
        return ll_res

    for a, b in zip(ll1.list_vals(), ll2.list_vals()):
        ll_res.add_in_tail(Node(a + b))

    return ll_res


class TestSumLinkedLists2(unittest.TestCase):

    def setUp(self):
        # Redirect stderr to capture error messages
        self.stderr = StringIO()
        self.original_stderr = sys.stderr
        sys.stderr = self.stderr

    def tearDown(self):
        # Reset stderr
        sys.stderr = self.original_stderr

    def create_linked_list(self, values):
        ll = LinkedList()
        for value in values:
            ll.add_in_tail(Node(value))
        return ll

    def test_equal_length_positive_values(self):
        ll1 = self.create_linked_list([1, 2, 3])
        ll2 = self.create_linked_list([4, 5, 6])
        expected = [5, 7, 9]
        result = sum_linked_lists2(ll1, ll2)
        self.assertEqual(result.list_vals(), expected)

    def test_equal_length_negative_values(self):
        ll1 = self.create_linked_list([-1, -2, -3])
        ll2 = self.create_linked_list([-4, -5, -6])
        expected = [-5, -7, -9]
        result = sum_linked_lists2(ll1, ll2)
        self.assertEqual(result.list_vals(), expected)

    def test_equal_length_mixed_values(self):
        ll1 = self.create_linked_list([1, -2, 3])
        ll2 = self.create_linked_list([-4, 5, -6])
        expected = [-3, 3, -3]
        result = sum_linked_lists2(ll1, ll2)
        self.assertEqual(result.list_vals(), expected)

    def test_empty_lists(self):
        ll1 = self.create_linked_list([])
        ll2 = self.create_linked_list([])
        expected = []
        result = sum_linked_lists2(ll1, ll2)
        self.assertEqual(result.list_vals(), expected)
        self.assertIn("Lists are empty.", self.stderr.getvalue())

    def test_different_lengths(self):
        ll1 = self.create_linked_list([1, 2])
        ll2 = self.create_linked_list([1, 2, 3])
        expected = []
        result = sum_linked_lists2(ll1, ll2)
        self.assertEqual(result.list_vals(), expected)
        self.assertIn("Lengths of lists are not equal.", self.stderr.getvalue())

    def test_none_list(self):
        ll1 = None
        ll2 = self.create_linked_list([1, 2, 3])
        expected = []
        result = sum_linked_lists2(ll1, ll2)
        self.assertEqual(result.list_vals(), expected)
        self.assertIn("Bad data.", self.stderr.getvalue())

    def test_equal_length_zero_values(self):
        ll1 = self.create_linked_list([0, 0, 0])
        ll2 = self.create_linked_list([0, 0, 0])
        expected = [0, 0, 0]
        result = sum_linked_lists2(ll1, ll2)
        self.assertEqual(result.list_vals(), expected)

if __name__ == '__main__':
    unittest.main()
