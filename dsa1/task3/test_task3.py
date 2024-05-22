import unittest
from task3 import DynArray


class TestDynArrayDelete(unittest.TestCase):
    def setUp(self):
        self.dyn_array = DynArray()
        for i in range(16):
            self.dyn_array.append(i)
        self.assertEqual(self.dyn_array[0], 0)
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_delete_from_empty_array(self):
        da = DynArray()
        with self.assertRaises(IndexError):
            da.delete(0)

    # it was the first bug
    def test_delete_only_one(self):
        da = DynArray()
        da.append(0)
        da.delete(0)
        self.assertEqual(da.list_vals(), [])
        self.assertEqual(da.capacity, 16)

        da = DynArray()
        da.append(0)
        with self.assertRaises(IndexError):
            da.delete(1)

    def test_delete_many_to_one_one_to_zero(self):
        da = DynArray()
        da.append(0)
        da.append(1)
        da.delete(1)
        self.assertListEqual(da.list_vals(), [0])
        da.delete(0)
        self.assertListEqual(da.list_vals(), [])

    def test_delete_from_start(self):
        self.dyn_array.delete(0)
        self.assertEqual(self.dyn_array.list_vals(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(len(self.dyn_array), 15)
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_delete_from_middle(self):
        self.dyn_array.delete(4)
        self.assertEqual(self.dyn_array.list_vals(), [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(len(self.dyn_array), 15)
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_delete_from_end(self):
        self.dyn_array.delete(self.dyn_array.count - 1)
        self.assertEqual(self.dyn_array.list_vals(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ])
        self.assertEqual(len(self.dyn_array), 15)
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_delete_invalid_high_index(self):
        with self.assertRaises(IndexError):
            self.dyn_array.delete(100)

    def test_delete_invalid_negative_index(self):
        with self.assertRaises(IndexError):
            self.dyn_array.delete(-1)

    def test_delete_small_series_without_resize(self) -> None:
        da: DynArray = DynArray()
        for i in range(10):
            da.append(i)
        da.delete(5)
        self.assertListEqual(da.list_vals(), [0, 1, 2, 3, 4, 6, 7, 8, 9])
        self.assertEqual(da.capacity, 16)

    def test_delete_series_without_resize(self):
        da = DynArray()
        num_el = 16
        for i in range(num_el):
            da.append(i)

        for i in range(num_el):
            da.delete(0)
        self.assertListEqual(da.list_vals(), [])
        self.assertEqual(da.capacity, 16)

    def test_delete_to_empty_and_add_again(self) -> None:
        da: DynArray = DynArray()
        for i in range(10):
            da.append(i)
        for _ in range(10):
            da.delete(0)
        self.assertListEqual(da.list_vals(), [])
        da.append(100)
        self.assertListEqual(da.list_vals(), [100])
        self.assertEqual(da.capacity, 16)

    def test_delete_series_with_resize(self):
        da = DynArray()
        for i in range(32):
            da.append(i)
        self.assertEqual(da.capacity, 32)

        for i in range(32):
            da.delete(0)
        self.assertListEqual(da.list_vals(), [])
        self.assertEqual(da.capacity, 16)

    def test_delete_multiple_elements_successively(self) -> None:
        da: DynArray = DynArray()
        for i in range(20):
            da.append(i)
        for _ in range(5):
            da.delete(0)
        self.assertListEqual(da.list_vals(), list(range(5, 20)))

    def test_delete_causing_capacity_reduction(self) -> None:
        da: DynArray = DynArray()
        for i in range(32):
            da.append(i)
        for _ in range(25):
            da.delete(0)
        self.assertListEqual(da.list_vals(), list(range(25, 32)))
        self.assertEqual(da.capacity, 16)

    def test_delete_every_other_element(self) -> None:
        da: DynArray = DynArray()
        for i in range(10):
            da.append(i)
        for i in range(5):
            da.delete(i)
        self.assertListEqual(da.list_vals(), [1, 3, 5, 7, 9])
        self.assertEqual(da.capacity, 16)


class TestDynArray(unittest.TestCase):

    def test_init(self):
        da = DynArray()
        self.assertEqual(da.count, 0)
        self.assertEqual(da.capacity, 16)

    def test_insert(self):
        da = DynArray()
        da.append(0)
        da.append(1)

        da.insert(0, 2)
        self.assertListEqual(da.list_vals(), [2, 0, 1])

        with self.assertRaises(IndexError):
            da.insert(-1, 0)
        with self.assertRaises(IndexError):
            da.insert(12, 0)

        da = DynArray()
        da.append(0)
        da.append(1)
        da.insert(2, 2)
        self.assertListEqual(da.list_vals(), [0, 1, 2])

        da = DynArray()
        for i in range(16):
            da.append(i)
        self.assertEqual(da.count, 16)
        self.assertEqual(da.capacity, 16)
        da.insert(0, 2)
        self.assertEqual(da.count, 17)
        self.assertEqual(da.capacity, 32)


if __name__ == "__main__":
    unittest.main()
