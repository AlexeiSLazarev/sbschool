from typing import Optional, Any


class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, value: str) -> int:
        hk1: int = 0
        for ch in value:
            hk1 += ord(ch)
        return hk1 % self.size

    def seek_slot(self, value: str) -> Optional[int]:
        base_id: int = self.hash_fun(value)
        for i in range(self.size):
            key_id: int = base_id + i
            if key_id >= self.size:
                key_id = key_id - self.size
            if self.keys[key_id] is None:
                return key_id

    def find(self, value: str) -> Optional[int]:
        base_id: int = self.hash_fun(value)
        for i in range(self.size):
            slot_id: int = base_id + i
            if slot_id >= self.size:
                slot_id = slot_id - self.size
            if self.keys[slot_id] == value:
                return slot_id
        return None

    def is_key(self, key) -> bool:
        for x in self.keys:
            if x == key:
                return True
        return False

    def get_key_id(self, key: Any) -> Optional[int]:
        for key_id, x in enumerate(self.keys):
            if x == key:
                return key_id
        return None

    def put(self, key, value):
        if self.is_key(key):
            key_id: int = self.get_key_id(key)
            self.values[key_id] = value
            return

        key_id: Optional[int] = self.seek_slot(key)
        if key_id is not None:
            self.keys[key_id] = key
            self.values[key_id] = value

    def get(self, key: str) -> Optional[Any]:
        key_id = self.get_key_id(key)
        if key_id is not None:
            return self.values[key_id]
        return None
