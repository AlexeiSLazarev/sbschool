import unittest
from task11 import BitArray, BloomFilter


class TestBitArray(unittest.TestCase):

    def test_is_subset(self):
        bit_array1 = BitArray()
        bit_array1.set_bit(1)
        bit_array2 = BitArray()
        bit_array2.set_bit(1)
        bit_array2.set_bit(3)
        self.assertTrue(bit_array1.is_subset(bit_array2))

        bit_array1 = BitArray()
        bit_array1.set_bit(1)
        bit_array1.set_bit(3)
        bit_array1.set_bit(6)
        bit_array2 = BitArray()
        bit_array2.set_bit(1)
        bit_array2.set_bit(3)
        bit_array2.set_bit(6)
        bit_array2.set_bit(8)
        self.assertTrue(bit_array1.is_subset(bit_array2))

    def test_is_not_subset(self):
        bit_array1 = BitArray()
        bit_array1.set_bit(1)
        bit_array1.set_bit(4)
        bit_array2 = BitArray()
        bit_array2.set_bit(1)
        bit_array2.set_bit(3)
        self.assertFalse(bit_array1.is_subset(bit_array2))

    def test_bit_operations(self):
        # Test case 1: Create a BitArray with size 1 and initialize it from_integer
        bit_array1 = BitArray(1)
        self.assertEqual(bit_array1.to_integer(), 1)

        # Test case 2: Create a BitArray with size 2 and initialize it from_integer
        bit_array2 = BitArray(3)
        self.assertEqual(bit_array2.to_integer(), 3)

        # Test case 3: Perform bitwise AND operation
        result_and = bit_array1 & bit_array2
        self.assertEqual(result_and.to_integer(), 1 & 3)

        # Test case 4: Perform bitwise OR operation
        result_or = bit_array1 | bit_array2
        self.assertEqual(result_or.to_integer(), 1 | 3)

        # Test case 5: Check if the sizes of resulting BitArrays are correct
        self.assertEqual(result_and.size, max(bit_array1.size, bit_array2.size))
        self.assertEqual(result_or.size, max(bit_array1.size, bit_array2.size))

    def test_invalid_index(self):
        # Test case 1: Try to set a bit at an invalid index
        bit_array = BitArray(32)
        with self.assertRaises(IndexError):
            bit_array.set_bit(32)

        # Test case 2: Try to clear a bit at an invalid index
        with self.assertRaises(IndexError):
            bit_array.clear_bit(-1)

        # Test case 3: Try to check a bit at an invalid index
        with self.assertRaises(IndexError):
            bit_array.check_bit(33)

    def test_bit_array_size(self):
        # Test case 1: Check the size of a BitArray with default size
        bit_array1 = BitArray()
        self.assertEqual(bit_array1.size, 32)

        # Test case 2: Check the size of a BitArray with custom size
        bit_array2 = BitArray(64)
        self.assertEqual(bit_array2.to_integer(), 64)


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

    def test_filter_mask(self):
        for test_str in self.test_strings:
            self.bloom_filter.add(test_str)
        filter_mask = self.bloom_filter.filter_mask
        for test_str in self.test_strings:
            self.assertTrue(filter_mask.check_bit(self.bloom_filter.hash1(test_str)))
            self.assertTrue(filter_mask.check_bit(self.bloom_filter.hash2(test_str)))

    def test_invalid_argument_type(self):
        with self.assertRaises(TypeError):
            self.bloom_filter.add(123)

        with self.assertRaises(TypeError):
            self.bloom_filter.is_value(123)

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
