import unittest
from task5 import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_on_empty_queue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.get_first().value, 1)
        self.assertEqual(self.queue.get_last().value, 1)

    def test_enqueue_on_non_empty_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.get_first().value, 1)
        self.assertEqual(self.queue.get_last().value, 3)

    def test_dequeue_on_empty_queue(self):
        result = self.queue.dequeue()
        self.assertIsNone(result)
        self.assertEqual(self.queue.size(), 0)

    def test_dequeue_on_queue_with_one_element(self):
        self.queue.enqueue(1)
        result = self.queue.dequeue()
        self.assertEqual(result, 1)
        self.assertEqual(self.queue.size(), 0)

    def test_dequeue_on_queue_with_multiple_elements(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        result1 = self.queue.dequeue()
        result2 = self.queue.dequeue()
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.get_first().value, 3)
        self.assertEqual(self.queue.get_last().value, 3)

    def test_size_on_empty_queue(self):
        self.assertEqual(self.queue.size(), 0)

    def test_size_on_non_empty_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)

    def test_list_vals(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.list_vals(), [1, 2, 3])

    def test_rotation(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.assertEqual(self.queue.list_vals(), [1, 2, 3, 4])

    def test_rotate_empty_queue(self):
        self.queue.rotate(3)
        self.assertEqual(self.queue.list_vals(), [])

    def test_rotate_single_element_queue(self):
        self.queue.enqueue(1)
        self.queue.rotate(1)
        self.assertEqual(self.queue.list_vals(), [1])

    def test_rotate_multiple_elements_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.rotate(1)
        self.assertEqual(self.queue.list_vals(), [2, 3, 1])

    def test_rotate_multiple_elements_queue_multiple_steps(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.rotate(2)
        self.assertEqual(self.queue.list_vals(), [3, 4, 1, 2])

    def test_rotate_multiple_elements_queue_more_than_length(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.rotate(5)
        self.assertEqual(self.queue.list_vals(), [2, 3, 4, 1])

    def test_rotate_back_to_original(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.rotate(4)
        self.assertEqual(self.queue.list_vals(), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
