import unittest
from task11 import BloomFilter


class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bloom_filter = BloomFilter(f_len=32)
        self.test_strings = [
            "0123456789",
            "1234567890",
            "2345678901",
            "3456789012",
            "4567890123",
            "5678901234",
            "6789012345",
            "7890123456",
            "8901234567",
            "9012345678"
        ]

    def test_add_and_is_value(self):
        for test_str in self.test_strings:
            self.bloom_filter.add(test_str)
        for test_str in self.test_strings:
            self.assertTrue(self.bloom_filter.is_value(test_str))
        self.assertFalse(self.bloom_filter.is_value("9999999999"))

    def test_base_func1(self):
        bloom_filter = BloomFilter()
        bloom_filter.add("abba")
        bloom_filter.add("acdc")
        bloom_filter.add("Metallica")
        bloom_filter.add("Manowar")
        self.assertTrue(bloom_filter.is_value("abba"))
        self.assertFalse(bloom_filter.is_value("Deep Purple"))
        self.assertFalse(bloom_filter.is_value("Joe Satriani"))


if __name__ == '__main__':
    unittest.main()
