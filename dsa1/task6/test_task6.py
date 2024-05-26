import unittest
from task6 import Deque, Node
import unittest


class TestDeque(unittest.TestCase):

    def setUp(self):
        self.deque = Deque()

    def test_initial_size(self):
        self.assertEqual(self.deque.size(), 0)

    def test_add_front_to_empty_deque(self):
        self.deque.addFront(10)
        self.assertEqual(self.deque.size(), 1)

    def test_add_tail_to_empty_deque(self):
        self.deque.addTail(20)
        self.assertEqual(self.deque.size(), 1)

    def test_add_front_and_tail(self):
        self.deque.addFront(10)
        self.deque.addTail(20)
        self.assertEqual(self.deque.size(), 2)

    def test_remove_front_from_single_element_deque(self):
        self.deque.addFront(10)
        self.assertEqual(self.deque.removeFront(), 10)
        self.assertEqual(self.deque.size(), 0)

    def test_remove_tail_from_single_element_deque(self):
        self.deque.addTail(20)
        self.assertEqual(self.deque.removeTail(), 20)
        self.assertEqual(self.deque.size(), 0)

    def test_remove_front_from_multi_element_deque(self):
        self.deque.addFront(10)
        self.deque.addTail(20)
        self.assertEqual(self.deque.removeFront(), 10)
        self.assertEqual(self.deque.size(), 1)

    def test_remove_tail_from_multi_element_deque(self):
        self.deque.addFront(10)
        self.deque.addTail(20)
        self.assertEqual(self.deque.removeTail(), 20)
        self.assertEqual(self.deque.size(), 1)

    def test_add_front_and_tail_and_remove(self):
        self.deque.addFront(10)
        self.deque.addTail(20)
        self.deque.addFront(30)
        self.deque.addTail(40)
        self.assertEqual(self.deque.size(), 4)

        self.assertEqual(self.deque.removeFront(), 30)
        self.assertEqual(self.deque.size(), 3)

        self.assertEqual(self.deque.removeTail(), 40)
        self.assertEqual(self.deque.size(), 2)

    def test_remove_from_empty_deque(self):
        self.assertEqual(self.deque.size(), 0)
        self.assertIsNone(self.deque.removeFront())
        self.assertIsNone(self.deque.removeTail())


if __name__ == '__main__':
    unittest.main()
