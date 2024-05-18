from task1 import LinkedList, Node
from typing import List, Dict, Union
import unittest


def sum_linked_lists(ll1: LinkedList, ll2: LinkedList) -> Dict[str, Union[List[int], str]]:
    """
    The function takes two linked lists and if their lengths are equal,
    returns a new list where each element is the sum of corresponding elements from the input lists.
    Function returns the result list and a message.
    The message indicates success of processing or a risen problem.
    """

    if ll1 is None or ll2 is None:
        return {"value": [], "message": "Bad data."}

    l1: int = ll1.len()
    l2: int = ll2.len()

    if l1 != l2: return {"value": [], "message": "Lengths of lists are not equal."}
    if l1 == 0: return {"value": [], "message": "Lists are empty."}
    return {"value": [a + b for a, b in zip(ll1.list_vals(), ll2.list_vals())], "message": "Done."}


class TestSumLinkedLists(unittest.TestCase):
    def test_sum_equal_length(self):
        ll1 = LinkedList()
        ll2 = LinkedList()

        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(2))
        ll1.add_in_tail(Node(3))

        ll2.add_in_tail(Node(4))
        ll2.add_in_tail(Node(5))
        ll2.add_in_tail(Node(6))

        result = sum_linked_lists(ll1, ll2)
        self.assertEqual(result["value"], [5, 7, 9])
        self.assertEqual(result["message"], "Done.")

    def test_sum_different_length(self):
        ll1 = LinkedList()
        ll2 = LinkedList()

        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(2))

        ll2.add_in_tail(Node(4))
        ll2.add_in_tail(Node(5))
        ll2.add_in_tail(Node(6))

        result = sum_linked_lists(ll1, ll2)
        self.assertEqual(result["value"], [])
        self.assertEqual(result["message"], "Lengths of lists are not equal.")

    def test_sum_empty_lists(self):
        ll1 = LinkedList()
        ll2 = LinkedList()

        result = sum_linked_lists(ll1, ll2)
        self.assertEqual(result["value"], [])
        self.assertEqual(result["message"], "Lists are empty.")

    def test_sum_none_list(self):
        ll1 = None
        ll2 = LinkedList()

        result = sum_linked_lists(ll1, ll2)
        self.assertEqual(result["value"], [])
        self.assertEqual(result["message"], "Bad data.")

        ll1 = LinkedList()
        ll2 = None

        result = sum_linked_lists(ll1, ll2)
        self.assertEqual(result["value"], [])
        self.assertEqual(result["message"], "Bad data.")


if __name__ == '__main__':
    unittest.main()
