import unittest
from task7 import OrderedList, OrderedStringList


class TestOrderedList(unittest.TestCase):

    def test_add_val_to_empty(self):
        ord_list = OrderedList()
        ord_list.add(1)
        self.assertEqual(ord_list.len(), 1)
        self.assertListEqual(ord_list.list_vals(), [1])

    def test_add_same_vals(self):
        ord_list = OrderedList()
        ord_list.add(1)
        ord_list.add(1)
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), [1, 1])

        ord_list.add(1)
        ord_list.add(1)
        self.assertEqual(ord_list.len(), 4)
        self.assertListEqual(ord_list.list_vals(), [1, 1, 1, 1])

    def test_asc(self):
        ord_list = OrderedList(True)
        ord_list.add(4)
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        self.assertEqual(ord_list.len(), 4)
        self.assertListEqual(ord_list.list_vals(), [1, 2, 3, 4])

    def test_desc(self):
        ord_list = OrderedList(False)
        ord_list.add(1)
        ord_list.add(4)
        ord_list.add(2)
        ord_list.add(3)
        self.assertEqual(ord_list.len(), 4)
        self.assertListEqual(ord_list.list_vals(), [4, 3, 2, 1])

    def test_delete(self):
        ord_list = OrderedList(True)
        ord_list.add(1)
        ord_list.add(4)
        ord_list.add(2)
        ord_list.add(3)
        ord_list.delete(3)
        self.assertListEqual(ord_list.list_vals(), [1, 2, 4])
        self.assertEqual(ord_list.len(), 3)

    def test_find(self):
        ord_list = OrderedList(True)
        ord_list.add(1)
        ord_list.add(4)
        ord_list.add(2)
        ord_list.add(3)
        node = ord_list.find(3)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 3)

        node = ord_list.find(5)
        self.assertIsNone(node)

    def test_clean(self):
        ord_list = OrderedList(True)
        ord_list.add(1)
        ord_list.add(4)
        ord_list.clean(False)
        self.assertEqual(ord_list.len(), 0)
        self.assertListEqual(ord_list.list_vals(), [])

    def test_get_all(self):
        ord_list = OrderedList(True)
        ord_list.add(1)
        ord_list.add(4)
        nodes = ord_list.get_all()
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].value, 1)
        self.assertEqual(nodes[1].value, 4)

    def test_add_to_one_element(self):
        ord_list = OrderedList()
        ord_list.add(2)
        ord_list.add(1)
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), [1, 2])

    def test_add_to_many_elements(self):
        ord_list = OrderedList()
        ord_list.add(3)
        ord_list.add(1)
        ord_list.add(2)
        self.assertEqual(ord_list.len(), 3)
        self.assertListEqual(ord_list.list_vals(), [1, 2, 3])

    def test_find_in_empty(self):
        ord_list = OrderedList()
        self.assertIsNone(ord_list.find(1))

    def test_find_in_one_element(self):
        ord_list = OrderedList()
        ord_list.add(1)
        self.assertIsNotNone(ord_list.find(1))
        self.assertIsNone(ord_list.find(2))

    def test_find_in_many_elements(self):
        ord_list = OrderedList()
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        self.assertIsNotNone(ord_list.find(2))
        self.assertIsNone(ord_list.find(4))

    def test_delete_from_empty(self):
        ord_list = OrderedList()
        ord_list.delete(1)
        self.assertEqual(ord_list.len(), 0)
        self.assertListEqual(ord_list.list_vals(), [])

    def test_delete_from_one_element(self):
        ord_list = OrderedList()
        ord_list.add(1)
        ord_list.delete(1)
        self.assertEqual(ord_list.len(), 0)
        self.assertListEqual(ord_list.list_vals(), [])

    def test_delete_from_many_elements(self):
        ord_list = OrderedList()
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        ord_list.delete(2)
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), [1, 3])
        ord_list.delete(1)
        self.assertEqual(ord_list.len(), 1)
        self.assertListEqual(ord_list.list_vals(), [3])
        ord_list.delete(3)
        self.assertEqual(ord_list.len(), 0)
        self.assertListEqual(ord_list.list_vals(), [])

    def test_get_all_empty(self):
        ord_list = OrderedList()
        self.assertEqual(len(ord_list.get_all()), 0)

    def test_get_all_one_element(self):
        ord_list = OrderedList()
        ord_list.add(1)
        nodes = ord_list.get_all()
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].value, 1)

    def test_get_all_many_elements(self):
        ord_list = OrderedList()
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        nodes = ord_list.get_all()
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].value, 1)
        self.assertEqual(nodes[1].value, 2)
        self.assertEqual(nodes[2].value, 3)

    def test_add_ascending(self):
        ord_list = OrderedList(True)
        ord_list.add(3)
        ord_list.add(1)
        ord_list.add(2)
        self.assertEqual(ord_list.len(), 3)
        self.assertListEqual(ord_list.list_vals(), [1, 2, 3])

    def test_add_descending(self):
        ord_list = OrderedList(False)
        ord_list.add(3)
        ord_list.add(1)
        ord_list.add(2)
        self.assertEqual(ord_list.len(), 3)
        self.assertListEqual(ord_list.list_vals(), [3, 2, 1])

        ord_list = OrderedList(False)
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        self.assertEqual(ord_list.len(), 3)
        self.assertListEqual(ord_list.list_vals(), [3, 2, 1])

    # Find tests
    def test_find_ascending(self):
        ord_list = OrderedList(True)
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        self.assertIsNotNone(ord_list.find(2))
        self.assertIsNone(ord_list.find(4))

    def test_find_descending(self):
        ord_list = OrderedList(False)
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        self.assertIsNotNone(ord_list.find(2))
        self.assertIsNone(ord_list.find(0))

    # Delete tests
    def test_delete_ascending(self):
        ord_list = OrderedList(True)
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        ord_list.delete(2)
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), [1, 3])

    def test_delete_descending(self):
        ord_list = OrderedList(False)
        ord_list.add(1)
        ord_list.add(2)
        ord_list.add(3)
        self.assertListEqual(ord_list.list_vals(), [3, 2, 1])
        ord_list.delete(2)
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), [3, 1])


class TestOrderedStringList(unittest.TestCase):

    def test_add_val_to_empty(self):
        ord_list = OrderedStringList()
        ord_list.add("Hello")
        self.assertEqual(ord_list.len(), 1)
        self.assertListEqual(ord_list.list_vals(), ["Hello"])

    def test_asc_desc(self):
        ord_list = OrderedStringList()
        ord_list.add("Hello")
        ord_list.add("World")
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), ["Hello", "World"])

        ord_list = OrderedStringList(False)
        ord_list.add("Hello")
        ord_list.add("World")
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), ["World", "Hello", ])

    def test_add_val_to_many_elements(self):
        ord_list = OrderedStringList()
        ord_list.add("Banana")
        ord_list.add("Apple")
        ord_list.add("Cherry")
        self.assertEqual(ord_list.len(), 3)
        self.assertListEqual(ord_list.list_vals(), ["Apple", "Banana", "Cherry"])

    def test_find_in_empty(self):
        ord_list = OrderedStringList()
        self.assertIsNone(ord_list.find("Hello"))

    def test_find_in_one_element(self):
        ord_list = OrderedStringList()
        ord_list.add("Hello")
        self.assertIsNotNone(ord_list.find("Hello"))
        self.assertIsNone(ord_list.find("World"))

    def test_find_in_many_elements(self):
        ord_list = OrderedStringList()
        ord_list.add("Apple")
        ord_list.add("Banana")
        ord_list.add("Cherry")
        self.assertIsNotNone(ord_list.find("Banana"))
        self.assertIsNone(ord_list.find("Date"))

    def test_delete_from_empty(self):
        ord_list = OrderedStringList()
        ord_list.delete("Hello")
        self.assertEqual(ord_list.len(), 0)
        self.assertListEqual(ord_list.list_vals(), [])

    def test_delete_from_one_element(self):
        ord_list = OrderedStringList()
        ord_list.add("Hello")
        ord_list.delete("Hello")
        self.assertEqual(ord_list.len(), 0)
        self.assertListEqual(ord_list.list_vals(), [])

    def test_delete_from_many_elements(self):
        ord_list = OrderedStringList()
        ord_list.add("Apple")
        ord_list.add("Banana")
        ord_list.add("Cherry")
        ord_list.delete("Banana")
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), ["Apple", "Cherry"])
        ord_list.delete("Apple")
        self.assertEqual(ord_list.len(), 1)
        self.assertListEqual(ord_list.list_vals(), ["Cherry"])
        ord_list.delete("Cherry")
        self.assertEqual(ord_list.len(), 0)
        self.assertListEqual(ord_list.list_vals(), [])

    def test_get_all_empty(self):
        ord_list = OrderedStringList()
        self.assertEqual(len(ord_list.get_all()), 0)

    def test_get_all_one_element(self):
        ord_list = OrderedStringList()
        ord_list.add("Hello")
        nodes = ord_list.get_all()
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].value, "Hello")

    def test_get_all_many_elements(self):
        ord_list = OrderedStringList()
        ord_list.add("Apple")
        ord_list.add("Banana")
        ord_list.add("Cherry")
        nodes = ord_list.get_all()
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].value, "Apple")
        self.assertEqual(nodes[1].value, "Banana")
        self.assertEqual(nodes[2].value, "Cherry")

    def test_clean(self):
        ord_list = OrderedStringList(True)
        ord_list.add("Apple")
        ord_list.add("Banana")
        ord_list.clean(False)
        self.assertEqual(ord_list.len(), 0)
        self.assertListEqual(ord_list.list_vals(), [])

    def test_add_ascending(self):
        ord_list = OrderedStringList(True)
        ord_list.add("Banana")
        ord_list.add("Apple")
        ord_list.add("Cherry")
        self.assertEqual(ord_list.len(), 3)
        self.assertListEqual(ord_list.list_vals(), ["Apple", "Banana", "Cherry"])

    def test_add_descending(self):
        ord_list = OrderedStringList(False)
        ord_list.add("Banana")
        ord_list.add("Apple")
        ord_list.add("Cherry")
        self.assertEqual(ord_list.len(), 3)
        self.assertListEqual(ord_list.list_vals(), ["Cherry", "Banana", "Apple"])

    # Find tests
    def test_find_ascending(self):
        ord_list = OrderedStringList(True)
        ord_list.add("Apple")
        ord_list.add("Banana")
        ord_list.add("Cherry")
        self.assertIsNotNone(ord_list.find("Banana"))
        self.assertIsNone(ord_list.find("Date"))

    def test_find_descending(self):
        ord_list = OrderedStringList(False)
        ord_list.add("Apple")
        ord_list.add("Banana")
        ord_list.add("Cherry")
        self.assertIsNotNone(ord_list.find("Banana"))
        self.assertIsNone(ord_list.find("Aardvark"))

    # Delete tests
    def test_delete_ascending(self):
        ord_list = OrderedStringList(True)
        ord_list.add("Apple")
        ord_list.add("Banana")
        ord_list.add("Cherry")
        ord_list.delete("Banana")
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), ["Apple", "Cherry"])

    def test_delete_descending(self):
        ord_list = OrderedStringList(False)
        ord_list.add("Apple")
        ord_list.add("Banana")
        ord_list.add("Cherry")
        ord_list.delete("Banana")
        self.assertEqual(ord_list.len(), 2)
        self.assertListEqual(ord_list.list_vals(), ["Cherry", "Apple"])


if __name__ == '__main__':
    unittest.main()
