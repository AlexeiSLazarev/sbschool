import unittest
from task12 import NativeCache
from random import randint

class MyTestCase(unittest.TestCase):
    def test_erase_keys(self):
        nc = NativeCache(5)
        for i in range(5):
            nc.put(f"str{i}", 1)

        for x in range(6):
            for i in range(x):
                nc.put(f"str{x}", 1)

        self.assertListEqual(nc.hits, [2,3,4,4,1])

if __name__ == '__main__':
    unittest.main()
