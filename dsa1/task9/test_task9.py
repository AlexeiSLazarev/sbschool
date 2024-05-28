import unittest
from task9 import NativeDictionary


class TestNativeDictionary(unittest.TestCase):
    def setUp(self):
        self.nd = NativeDictionary(5)

    def test_put_new_key(self):
        self.nd.put("apple", 1)
        self.assertEqual(self.nd.get("apple"), 1)

    def test_put_existing_key(self):
        self.nd.put("apple", 1)
        self.nd.put("apple", 2)
        self.assertEqual(self.nd.get("apple"), 2)

    def test_is_key(self):
        self.nd.put("apple", 1)
        self.assertTrue(self.nd.is_key("apple"))
        self.assertFalse(self.nd.is_key("banana"))

    def test_get(self):
        self.nd.put("apple", 1)
        self.assertEqual(self.nd.get("apple"), 1)
        self.assertIsNone(self.nd.get("banana"))

    def test_add_multiple_keys(self):
        self.nd.put("apple", 1)
        self.nd.put("banana", 3)
        self.nd.put("cherry", 4)
        self.assertEqual(self.nd.get("banana"), 3)
        self.assertEqual(self.nd.get("cherry"), 4)
        self.assertTrue(self.nd.is_key("banana"))
        self.assertTrue(self.nd.is_key("cherry"))

    def test_full(self):
        for i in range(5):
            self.nd.put(f"val{i}", i)
        for i in range(5):
            self.nd.put(f"val{i}", i)
        for i in range(5):
            self.assertEqual(self.nd.get(f"val{i}"), i)


if __name__ == '__main__':
    unittest.main()
