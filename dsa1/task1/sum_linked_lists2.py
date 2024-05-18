from io import StringIO

from task1 import Node, LinkedList
from typing import List, TextIO
import sys
import unittest


def sum_linked_lists2(ll1: LinkedList, ll2: LinkedList) -> List[int]:
    """
    The function takes two linked lists and if their lengths are equal,
    returns a new list where each element is the sum of corresponding elements from the input lists.
    Function returns the result list.
    All error messages are printed out in the stderr.
    """

    f: TextIO = sys.stderr

    if ll1 is None or ll2 is None:
        print("Bad data.", file=f)
        return []

    l1: int = ll1.len()
    l2: int = ll2.len()

    if l1 != l2:
        print("Lengths of lists are not equal.", file=f)
        return []

    if l1 == 0:
        print("Lists are empty.", file=f)
        return []

    return [a + b for a, b in zip(ll1.list_vals(), ll2.list_vals())]


class TestSumLinkedLists(unittest.TestCase):

    def test_sum_linked_lists2_bad_data(self):
        stderr_backup = sys.stderr
        sys.stderr = StringIO()
        self.assertEqual(sum_linked_lists2(None, None), [])
        self.assertEqual(sys.stderr.getvalue(), "Bad data.\n", "Summing None lists.")
        sys.stderr = stderr_backup

    def test_sum_linked_lists2_unequal_lengths(self):
        ll1 = LinkedList()
        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(2))

        ll2 = LinkedList()
        ll2.add_in_tail(Node(3))

        stderr_backup = sys.stderr
        sys.stderr = StringIO()
        result = sum_linked_lists2(ll1, ll2)
        expected_result = []
        self.assertEqual(result, expected_result)
        self.assertEqual(sys.stderr.getvalue(), "Lengths of lists are not equal.\n", "Summing unequal lists.")
        sys.stderr = stderr_backup

    def test_sum_linked_lists2_empty_lists(self):
        ll1 = LinkedList()
        ll2 = LinkedList()
        stderr_backup = sys.stderr
        sys.stderr = StringIO()
        result = sum_linked_lists2(ll1, ll2)
        self.assertEqual(result, [])
        self.assertEqual(sys.stderr.getvalue(), "Lists are empty.\n", "Summing empty lists.")
        sys.stderr = stderr_backup

    def test_sum_linked_lists2(self):
        ll1 = LinkedList()
        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(2))
        ll1.add_in_tail(Node(3))

        ll2 = LinkedList()
        ll2.add_in_tail(Node(4))
        ll2.add_in_tail(Node(5))
        ll2.add_in_tail(Node(6))

        stderr_backup = sys.stderr
        sys.stderr = StringIO()

        result = sum_linked_lists2(ll1, ll2)
        expected_result = [5, 7, 9]
        self.assertEqual(result, expected_result)
        self.assertEqual(sys.stderr.getvalue(), "", "Stderr should have an empty string.")

        sys.stderr = stderr_backup


if __name__ == '__main__':
    unittest.main()


