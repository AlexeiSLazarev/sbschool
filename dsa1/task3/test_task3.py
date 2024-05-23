import unittest
import random

from task3 import DynArray


class TestDeleteAndResize(unittest.TestCase):
    def test_delete_16(self):
        da: DynArray = DynArray()
        # check initial
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 0)

        # rise to 16. should be no change in capacity
        for i in range(16):
            da.append(i)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 16)
        self.assertEqual(da[15], 15)

        # delete first
        da.delete(0)
        self.assertEqual(da.list_vals(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(len(da), 15)
        self.assertEqual(da.capacity, 16)

        # delete last
        da.delete(14)
        self.assertEqual(da.list_vals(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,])
        self.assertEqual(len(da), 14)
        self.assertEqual(da.capacity, 16)

        # randomly delete all other elements
        for _ in range(len(da)):
            da.delete(random.randint(0, len(da) - 1))
        self.assertEqual(len(da), 0)
        self.assertEqual(da.capacity, 16)

    def test_delete_32(self):
        da: DynArray = DynArray()
        # check initial
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 0)

        # rise to 16. should be no change in capacity
        for i in range(32):
            da.append(i)
        self.assertEqual(da.capacity, 32)
        self.assertEqual(len(da), 32)
        self.assertEqual(da[23], 23)

        # delete first
        da.delete(0)
        self.assertEqual(da.list_vals(), list(range(1, 32)))
        self.assertEqual(len(da), 31)
        self.assertEqual(da.capacity, 32)

        # delete last
        da.delete(30)
        self.assertEqual(da.list_vals(), list(range(1, 31)))
        self.assertEqual(len(da), 30)
        self.assertEqual(da.capacity, 32)

        da: DynArray = DynArray()
        for i in range(32):
            da.append(i)
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 32)

        print("\n")
        for i in range(len(da) - 1):
            print(f"Step: {i}")
            print(f"Before: i: {i}, capacity: {da.capacity}, size: {len(da)}, emptiness: {da.capacity / da.count}")
            da.delete(random.randint(0, len(da) - 1))
            print(f"After: i: {i}, capacity: {da.capacity}, size: {len(da)}, emptiness: {da.capacity / da.count}")

            if i < 10:
                self.assertEqual(da.capacity, 32)
            # After: i = 10, size become 21 elements, emptiness > 1.5 -> resize to self.capacity / 1.5.
            # New size is 21 elements
            if 10 <= i < 18:
                self.assertEqual(da.capacity, 21)
            # After: i = 18, size become 14 elements, emptiness = 1.5 -> resize to self.capacity / 1.5.
            # New size is 16 elements
            if i >= 24:
                self.assertEqual(da.capacity, 16)


class TestDynArrayDelete(unittest.TestCase):
    def setUp(self) -> None:
        self.dyn_array: DynArray = DynArray()
        for i in range(16):
            self.dyn_array.append(i)
        self.assertEqual(self.dyn_array[0], 0)
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_delete_from_empty_array(self) -> None:
        da: DynArray = DynArray()
        with self.assertRaises(IndexError):
            da.delete(0)

    def test_delete_only_one(self) -> None:
        da: DynArray = DynArray()
        da.append(0)
        da.delete(0)
        self.assertEqual(da.list_vals(), [])
        self.assertEqual(da.capacity, 16)

        da = DynArray()
        da.append(0)
        with self.assertRaises(IndexError):
            da.delete(1)

    def test_delete_many_to_one_one_to_zero(self) -> None:
        da: DynArray = DynArray()
        da.append(0)
        da.append(1)
        da.delete(1)
        self.assertListEqual(da.list_vals(), [0])
        da.delete(0)
        self.assertListEqual(da.list_vals(), [])

    def test_delete_from_start(self) -> None:
        self.dyn_array.delete(0)
        self.assertEqual(self.dyn_array.list_vals(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(len(self.dyn_array), 15)
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_delete_from_middle(self) -> None:
        self.dyn_array.delete(4)
        self.assertEqual(self.dyn_array.list_vals(), [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(len(self.dyn_array), 15)
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_delete_from_end(self) -> None:
        self.dyn_array.delete(self.dyn_array.count - 1)
        self.assertEqual(self.dyn_array.list_vals(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(len(self.dyn_array), 15)
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_delete_invalid_high_index(self) -> None:
        with self.assertRaises(IndexError):
            self.dyn_array.delete(100)

    def test_delete_invalid_negative_index(self) -> None:
        with self.assertRaises(IndexError):
            self.dyn_array.delete(-1)

    def test_delete_small_series_without_resize(self) -> None:
        da: DynArray = DynArray()
        for i in range(10):
            da.append(i)
        da.delete(5)
        self.assertListEqual(da.list_vals(), [0, 1, 2, 3, 4, 6, 7, 8, 9])
        self.assertEqual(da.capacity, 16)

    def test_delete_series_without_resize(self) -> None:
        da: DynArray = DynArray()
        num_el: int = 16
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

    def test_delete_series_with_resize(self) -> None:
        da: DynArray = DynArray()
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

    def test_init(self) -> None:
        da: DynArray = DynArray()
        self.assertEqual(da.count, 0)
        self.assertEqual(da.capacity, 16)

    def test_insert(self) -> None:
        da: DynArray = DynArray()
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
