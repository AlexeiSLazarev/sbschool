from task10 import PowerSet
import unittest

import unittest
from time import time


class TestPowerSet(unittest.TestCase):

    def setUp(self):
        self.set1 = PowerSet()
        self.set2 = PowerSet()

    def test_put(self):
        self.set1.put(1)
        self.assertEqual(self.set1.size(), 1)
        self.set1.put(1)
        self.assertEqual(self.set1.size(), 1)
        self.set1.put(2)
        self.assertEqual(self.set1.size(), 2)

    def test_remove(self):
        self.set1.put(1)
        self.set1.put(2)
        self.assertTrue(self.set1.remove(1))
        self.assertFalse(self.set1.get(1))
        self.assertEqual(self.set1.size(), 1)
        self.assertFalse(self.set1.remove(3))

    def test_intersection(self):
        self.set1.put(1)
        self.set1.put(2)
        self.set2.put(2)
        self.set2.put(3)
        result = self.set1.intersection(self.set2)
        self.assertTrue(result.get(2))
        self.assertEqual(result.size(), 1)

        empty_set = self.set1.intersection(PowerSet())
        self.assertEqual(empty_set.size(), 0)

    def test_union(self):
        self.set1.put(1)
        self.set1.put(2)
        self.set2.put(2)
        self.set2.put(3)
        result = self.set1.union(self.set2)
        self.assertTrue(result.get(1))
        self.assertTrue(result.get(2))
        self.assertTrue(result.get(3))
        self.assertEqual(result.size(), 3)

        empty_union = self.set1.union(PowerSet())
        self.assertTrue(empty_union.get(1))
        self.assertTrue(empty_union.get(2))
        self.assertEqual(empty_union.size(), 2)

    def test_difference(self):
        self.set1.put(1)
        self.set1.put(2)
        self.set2.put(2)
        self.set2.put(3)
        result = self.set1.difference(self.set2)
        self.assertTrue(result.get(1))
        self.assertFalse(result.get(2))
        self.assertEqual(result.size(), 1)

        empty_diff = self.set1.difference(PowerSet())
        self.assertTrue(empty_diff.get(1))
        self.assertTrue(empty_diff.get(2))
        self.assertEqual(empty_diff.size(), 2)

    def test_issubset(self):
        self.set1.put(1)
        self.set1.put(2)
        self.set2.put(1)
        self.assertTrue(self.set1.issubset(self.set2))
        self.set2.put(2)
        self.assertTrue(self.set2.issubset(self.set1))
        self.set2.put(3)
        self.assertFalse(self.set1.issubset(self.set2))

    def test_performance(self):
        large_set1 = PowerSet()
        large_set2 = PowerSet()
        for i in range(20000):
            large_set1.put(i)
            if i % 2 == 0:
                large_set2.put(i)
        start_time = time()
        large_union = large_set1.union(large_set2)
        self.assertTrue(time() - start_time < 2)

        start_time = time()
        large_intersection = large_set1.intersection(large_set2)
        self.assertTrue(time() - start_time < 2)

        start_time = time()
        large_difference = large_set1.difference(large_set2)
        self.assertTrue(time() - start_time < 2)


if __name__ == '__main__':
    unittest.main()
