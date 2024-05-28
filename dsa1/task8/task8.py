class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str):
        hk1: int = 0
        for ch in value:
            hk1 += ord(ch)
        return hk1 % self.size

    def seek_slot(self, value):
        base_id: int = self.hash_fun(value)
        for i in range(self.step):
            slot_id = base_id + i * i
            if slot_id >= self.size:
                slot_id = slot_id - self.size
            if self.slots[slot_id] is None:
                return slot_id
        return None

    def put(self, value):
        slot_id = self.seek_slot(value)
        if slot_id is not None:
            self.slots[slot_id] = value
            return slot_id
        return None

    def find(self, value):
        base_id = self.hash_fun(value)
        for i in range(self.step):
            slot_id = base_id + i * i
            if slot_id >= self.size:
                slot_id = slot_id - self.size
            if self.slots[slot_id] == value:
                return slot_id
        return None
