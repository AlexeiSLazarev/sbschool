from typing import Optional


class HashTable:
    def __init__(self, sz: int, stp: int):
        self.size: int = sz
        self.step: int = stp
        self.slots: list[Optional[str]] = [None] * self.size

    def hash_fun(self, value: str) -> int:
        hk1: int = 0
        for ch in value:
            hk1 += ord(ch)
        return hk1 % self.size

    def seek_slot(self, value: str) -> Optional[int]:
        base_id: int = self.hash_fun(value)
        for i in range(self.step):
            slot_id: int = base_id + i * i
            if slot_id >= self.size:
                slot_id = slot_id - self.size
            if self.slots[slot_id] is None:
                return slot_id
        return None

    def put(self, value: str) -> Optional[int]:
        slot_id: Optional[int] = self.seek_slot(value)
        if slot_id is not None:
            self.slots[slot_id] = value
            return slot_id
        return None

    def find(self, value: str) -> Optional[int]:
        base_id: int = self.hash_fun(value)
        for i in range(self.step):
            slot_id: int = base_id + i * i
            if slot_id >= self.size:
                slot_id = slot_id - self.size
            if self.slots[slot_id] == value:
                return slot_id
        return None
