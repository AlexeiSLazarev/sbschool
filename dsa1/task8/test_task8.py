import unittest
from task8 import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.ht1 = HashTable(17, 3)
        self.ht2 = HashTable(19, 5)

    def test_empty_str(self):
        self.ht1.put("")
        slot_id = self.ht2.seek_slot("")
        self.assertEqual(slot_id, 0)

    def test_hash_fun(self):
        self.assertEqual(self.ht1.hash_fun("test"), sum(ord(ch) for ch in "test") % 17)
        self.assertEqual(self.ht2.hash_fun("test"), sum(ord(ch) for ch in "test") % 19)

    def test_seek_slot_empty(self):
        slot1 = self.ht1.seek_slot("test")
        self.assertIsNotNone(slot1)
        self.assertIsNone(self.ht1.slots[slot1])

        slot2 = self.ht2.seek_slot("test")
        self.assertIsNotNone(slot2)
        self.assertIsNone(self.ht2.slots[slot2])

    def test_put(self):
        slot1 = self.ht1.put("test")
        self.assertIsNotNone(slot1)
        self.assertEqual(self.ht1.slots[slot1], "test")

        slot2 = self.ht2.put("test")
        self.assertIsNotNone(slot2)
        self.assertEqual(self.ht2.slots[slot2], "test")

    def test_find_existing(self):
        slot1 = self.ht1.put("test")
        self.assertEqual(self.ht1.find("test"), slot1)

        slot2 = self.ht2.put("test")
        self.assertEqual(self.ht2.find("test"), slot2)

    def test_find_non_existing(self):
        self.assertIsNone(self.ht1.find("non_existing"))
        self.assertIsNone(self.ht2.find("non_existing"))

    def test_collision_handling(self):
        slot1_1 = self.ht1.put("test")
        slot1_2 = self.ht1.put("abc")  # Different string that might cause collision
        self.assertIsNotNone(slot1_1)
        self.assertIsNotNone(slot1_2)
        self.assertNotEqual(slot1_1, slot1_2)
        self.assertEqual(self.ht1.slots[slot1_1], "test")
        self.assertEqual(self.ht1.slots[slot1_2], "abc")

        slot2_1 = self.ht2.put("test")
        slot2_2 = self.ht2.put("abc")  # Different string that might cause collision
        self.assertIsNotNone(slot2_1)
        self.assertIsNotNone(slot2_2)
        self.assertNotEqual(slot2_1, slot2_2)
        self.assertEqual(self.ht2.slots[slot2_1], "test")
        self.assertEqual(self.ht2.slots[slot2_2], "abc")

    def test_put_until_full(self):
        for i in range(17):
            try:
                value = f"value{i}"
                slot = self.ht1.put(value)
                self.assertIsNotNone(slot)
                self.assertEqual(self.ht1.slots[slot], value)
            except:
                pass
        self.assertIsNone(self.ht1.put("extra_value"))

        for i in range(19):
            try:
                value = f"value{i}"
                slot = self.ht2.put(value)
                self.assertIsNotNone(slot)
                self.assertEqual(self.ht2.slots[slot], value)
            except:
                pass


if __name__ == '__main__':
    unittest.main()
