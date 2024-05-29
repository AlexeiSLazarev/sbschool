class BloomFilter:

    def __init__(self, f_len: int = 32) -> None:
        self.filter_len: int = f_len
        self.bit_array = 0

    def hash1(self, str1: str) -> int:
        rand_num: int = 17
        hk1: int = 0
        for ch in str1:
            hk1 = (hk1 * rand_num + ord(ch)) % self.filter_len
        return 1 << hk1

    def hash2(self, str1: str) -> int:
        rand_num: int = 223
        hk2: int = 0
        for ch in str1:
            hk2 = (hk2 * rand_num + ord(ch)) % self.filter_len
        return 1 << hk2

    def add(self, str1: str) -> None:
        self.bit_array = self.bit_array | self.get_mask(str1)

    def get_mask(self, str1: str) -> int:
        return self.hash1(str1) | self.hash2(str1)

    def is_value(self, str1: str) -> int:
        mask = self.get_mask(str1)
        return mask & self.bit_array == mask


