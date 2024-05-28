from typing import List, Any


class PowerSet:
    def __init__(self):
        self.set: List[Any] = []

    def size(self) -> int:
        return len(self.set)

    def put(self, value: Any) -> None:
        if value not in self.set:
            self.set.append(value)

    def get(self, value: Any) -> bool:
        return value in self.set

    def remove(self, value: Any) -> bool:
        if value in self.set:
            self.set.remove(value)
            return True
        return False

    def intersection(self, set2: 'PowerSet') -> 'PowerSet':
        intersection_list = [x for x in self.set if x in set2.set]
        result = PowerSet()
        result.set = intersection_list
        return result

    def union(self, set2: 'PowerSet') -> 'PowerSet':
        union_list = self.set[:]
        for x in set2.set:
            if x not in union_list:
                union_list.append(x)
        result = PowerSet()
        result.set = union_list
        return result

    def difference(self, set2: 'PowerSet') -> 'PowerSet':
        diff_list = [x for x in self.set if x not in set2.set]
        result = PowerSet()
        result.set = diff_list
        return result

    def issubset(self, set2: 'PowerSet') -> bool:
        for x in set2.set:
            if x not in self.set:
                return False
        return True


