class BitArray:
    def __init__(self, from_integer: int = None) -> None:
        self.size: int = 32
        self.array: List[int] = [0] * self.size
        if from_integer is not None:
            self.from_integer(from_integer)

    def clear_bit(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = 0

    def check_bit(self, index: int) -> int:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def set_bit(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = 1

    def from_integer(self, integer: int) -> None:
        for i in range(self.size):
            if integer & (1 << i):
                self.set_bit(i)

    def to_integer(self) -> int:
        result: int = 0
        for i in range(self.size):
            if self.check_bit(i):
                result |= 1 << i
        return result

    def __and__(self, other: 'BitArray') -> 'BitArray':
        if self.size != other.size:
            raise ValueError("BitArray sizes do not match")
        result: 'BitArray' = BitArray()
        for i in range(self.size):
            if self.check_bit(i) and other.check_bit(i):
                result.set_bit(i)
        return result

    def __or__(self, other: 'BitArray') -> 'BitArray':
        if self.size != other.size:
            raise ValueError("BitArray sizes do not match")
        result: 'BitArray' = BitArray()
        for i in range(self.size):
            if self.check_bit(i) or other.check_bit(i):
                result.set_bit(i)
        return result

    def is_subset(self, other: 'BitArray') -> bool:
        if self.size != other.size:
            raise ValueError("BitArray sizes do not match")
        for i in range(self.size):
            if self.check_bit(i) == 1:
                if self.check_bit(i) != other.check_bit(i):
                    return False
        return True

    def __str__(self) -> str:
        return ''.join(['1' if self.check_bit(i) else '0' for i in range(self.size)])


class BloomFilter:

    def __init__(self, f_len: int = 32) -> None:
        self.filter_len: int = f_len
        self.filter_mask: BitArray = BitArray()

    def hash1(self, str1: str) -> int:
        rand_num: int = 17
        hk1: int = 0
        for ch in str1:
            hk1 = (hk1 * rand_num + ord(ch)) % self.filter_len
        return hk1

    def hash2(self, str1: str) -> int:
        rand_num: int = 223
        hk1: int = 0
        for ch in str1:
            hk1 = (hk1 * rand_num + ord(ch)) % self.filter_len
        return hk1

    def add(self, str1: str) -> None:
        mask: BitArray = self.get_mask(str1)
        tmp: BitArray = self.filter_mask | mask
        self.filter_mask = tmp

    def get_mask(self, str1: str) -> BitArray:
        mask: BitArray = BitArray()
        mask.set_bit(self.hash1(str1))
        mask.set_bit(self.hash2(str1))
        return mask

    def is_value(self, str1: str) -> bool:
        mask: BitArray = self.get_mask(str1)
        return mask.is_subset(self.filter_mask)





