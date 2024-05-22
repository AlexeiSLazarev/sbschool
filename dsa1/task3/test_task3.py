import random
import unittest
from task3 import DynArray


class TestDynArrayDelete(unittest.TestCase):
    def setUp(self):
        self.dyn_array = DynArray()
        for i in range(10):
            self.dyn_array.append(i)
        self.initial_capacity = self.dyn_array.capacity

    def test_delete_from_start(self):
        self.dyn_array.delete(0)
        self.assertEqual(self.dyn_array.list_vals(), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(len(self.dyn_array), 9)
        self.assertEqual(self.dyn_array.capacity, self.initial_capacity)

    def test_delete_from_middle(self):
        self.dyn_array.delete(4)
        self.assertEqual(self.dyn_array.list_vals(), [0, 1, 2, 3, 5, 6, 7, 8, 9])
        self.assertEqual(len(self.dyn_array), 9)
        self.assertEqual(self.dyn_array.capacity, self.initial_capacity)

    def test_delete_from_end(self):
        self.dyn_array.delete(self.dyn_array.count - 1)
        self.assertEqual(self.dyn_array.list_vals(), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(len(self.dyn_array), 9)
        self.assertEqual(self.dyn_array.capacity, self.initial_capacity)

    def test_delete_invalid_high_index(self):
        with self.assertRaises(IndexError):
            self.dyn_array.delete(100)

    def test_delete_invalid_negative_index(self):
        with self.assertRaises(IndexError):
            self.dyn_array.delete(-1)

class TestDynArray(unittest.TestCase):

    def test_init(self):
        da = DynArray()
        self.assertEqual(da.count, 0)
        self.assertEqual(da.capacity, 16)

    def test_insert(self):
        da = DynArray()
        da.append(0)
        da.append(1)
        # Вставка элемента, когда размер буфера не превышен.
        da.insert(0, 2)
        self.assertListEqual(da.list_vals(), [2, 0, 1])

        # Попытка вставки элемента в недопустимую позицию.
        with self.assertRaises(IndexError):
            da.insert(-1, 0)
        with self.assertRaises(IndexError):
            da.insert(12, 0)

        # Вставка элемента, i == count
        # Вставка элемента, когда размер буфера превышен.
        da = DynArray()
        da.append(0)
        da.append(1)
        da.insert(2, 2)
        self.assertListEqual(da.list_vals(), [0, 1, 2])

        # Вставка элемента, когда размер буфера превышен.
        da = DynArray()
        for i in range(16):
            da.append(i)
        self.assertEqual(da.count, 16)
        self.assertEqual(da.capacity, 16)
        da.insert(0, 2)
        self.assertEqual(da.count, 17)
        self.assertEqual(da.capacity, 32)

    def test_delete(self):
        da = DynArray()
        da.append(0)
        da.append(1)
        # Генерирует исключение IndexError, если i выходит за пределы массива.
        with self.assertRaises(IndexError):
            da.delete(-1)
        with self.assertRaises(IndexError):
            da.delete(100)

        # Попытка удаления элемента в недопустимой позиции.
        da = DynArray()
        with self.assertRaises(IndexError):
            da.delete(0)

        # Удаление элемента, когда размер буфера не меняется.
        da.append(0)
        da.delete(0)
        self.assertEqual(da.count, 0)

        # Удаление последнего элемента
        da = DynArray()
        da.append(0)
        da.append(1)
        da.delete(1)
        self.assertListEqual(da.list_vals(), [0])

        # Удаление непоследнего элемента
        da = DynArray()
        da.append(0)
        da.append(1)
        da.append(2)
        da.delete(1)
        self.assertListEqual(da.list_vals(), [0, 2])

        # Удаление серии элементов
        da = DynArray()
        num_el = 32
        for i in range(num_el):
            da.append(i)

        for i in range(num_el):
            # print(f"\n Count: {da.count}, capacity: {da.capacity}")
            # for x in range(da.count):
            #     print(da[x], end=", ")
            # print("\n")
            da.delete(0)
        self.assertListEqual(da.list_vals(), [])

        # Удаление элемента, когда размер буфера уменьшается.
        da = DynArray()
        for i in range(32):
            da.append(i)
        self.assertEqual(da.capacity, 32)

        for i in range(32):
            da.delete(0)
        self.assertListEqual(da.list_vals(), [])
        self.assertEqual(da.capacity, 16)


if __name__ == "__main__":
    unittest.main()
