import random
import unittest
from task3 import DynArray


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
            print(f"\n Count: {da.count}, capacity: {da.capacity}")
            for x in range(da.count):
                print(da[x], end=", ")
            print("\n")
            da.delete(0)
        self.assertListEqual(da.list_vals(), [])

        # Удаление элемента, когда размер буфера уменьшается.
        # da = DynArray()
        # for i in range(32):
        #     da.append(i)
        # self.assertEqual(da.capacity, 32)
        #
        # for i in range(32):
        #     print(i, da.capacity)
        #     da.delete(i)
        # self.assertListEqual(da.list_vals(), [])
        # # self.assertEqual(da.capacity, 16)

if __name__ == "__main__":
    unittest.main()
