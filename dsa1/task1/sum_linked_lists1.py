from typing import Optional, Dict, Union
from task1 import LinkedList, Node
import unittest


def sum_linked_lists(ll1: Optional[LinkedList], ll2: Optional[LinkedList]) -> Dict[str, Union[LinkedList, str]]:
    """
    The function takes two linked lists and if their lengths are equal,
    returns a new linked list where each element is the sum of corresponding elements from the input lists.
    Function returns a dictionary containing the result linked list and a message.
    The message indicates the success of processing or a risen problem.
    """

    result_list = LinkedList()

    if ll1 is None or ll2 is None:
        return {"result": result_list, "message": "Bad data."}

    l1: int = ll1.len()
    l2: int = ll2.len()

    if l1 != l2:
        return {"result": result_list, "message": "Lengths of lists are not equal."}
    if l1 == 0:
        return {"result": result_list, "message": "Lists are empty."}

    for a, b in zip(ll1.list_vals(), ll2.list_vals()):
        result_list.add_in_tail(Node(a + b))

    return {"result": result_list, "message": "Done."}


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
        result_list = result["result"]
        message = result["message"]

        self.assertEqual(result_list.list_vals(), [5, 7, 9])
        self.assertEqual(message, "Done.")

    def test_sum_different_length(self):
        ll1 = LinkedList()
        ll2 = LinkedList()

        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(2))

        ll2.add_in_tail(Node(4))
        ll2.add_in_tail(Node(5))
        ll2.add_in_tail(Node(6))

        result = sum_linked_lists(ll1, ll2)
        result_list = result["result"]
        message = result["message"]

        self.assertEqual(result_list.list_vals(), [])
        self.assertEqual(message, "Lengths of lists are not equal.")

    def test_sum_empty_lists(self):
        ll1 = LinkedList()
        ll2 = LinkedList()

        result = sum_linked_lists(ll1, ll2)
        result_list = result["result"]
        message = result["message"]

        self.assertEqual(result_list.list_vals(), [])
        self.assertEqual(message, "Lists are empty.")

    def test_sum_none_list(self):
        ll1 = None
        ll2 = LinkedList()

        result = sum_linked_lists(ll1, ll2)
        result_list = result["result"]
        message = result["message"]

        self.assertEqual(result_list.list_vals(), [])
        self.assertEqual(message, "Bad data.")

        ll1 = LinkedList()
        ll2 = None

        result = sum_linked_lists(ll1, ll2)
        result_list = result["result"]
        message = result["message"]

        self.assertEqual(result_list.list_vals(), [])
        self.assertEqual(message, "Bad data.")


if __name__ == '__main__':
    unittest.main()
