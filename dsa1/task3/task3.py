import ctypes
from typing import Any, List


class DynArray:

    def __init__(self) -> None:
        self.count: int = 0
        self.capacity: int = 16
        self.upsize_coef: int = 2
        self.downsize_coef: float = 1.5
        self.array: Any = self.make_array(self.capacity)

    def reset(self) -> None:
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self) -> int:
        return self.count

    def make_array(self, new_capacity: int) -> Any:
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i: int) -> Any:
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity: int) -> None:
        if new_capacity < 16:
            new_capacity = 16
        new_array: Any = self.make_array(new_capacity)

        for i in range(min(self.count, new_capacity)):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm: Any) -> None:
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def shift_vals_from_i(self, i: int) -> None:
        cur_index = self.count
        while cur_index > i:
            self.array[cur_index] = self.array[cur_index - 1]
            cur_index -= 1

    def shift_vals_to_i(self, i: int) -> None:
        while i < self.count - 1:
            self.array[i] = self.array[i + 1]
            i += 1

    def insert(self, i: int, itm: Any) -> None:
        if i < 0 or i > self.count:
            raise IndexError('Wrong index.')

        if self.count >= self.capacity:
            self.resize(self.capacity * self.upsize_coef)

        self.shift_vals_from_i(i)
        self.array[i] = itm
        self.count += 1

    def delete(self, i: int) -> None:
        if i < 0 or i >= self.count:
            raise IndexError('Wrong index.')

        # Shift values to the left
        self.shift_vals_to_i(i)
        self.array[self.count - 1] = None
        self.count -= 1

        # Resize if the array is less than `downsize_coef` full
        if self.capacity > 16 and self.count > 0:
            if (self.capacity / self.count) > self.downsize_coef:
                self.resize(max(16, int(self.capacity / self.downsize_coef)))

    def list_vals(self) -> List[Any]:
        return [self.array[i] for i in range(self.count)]

    def print_vals(self) -> None:
        for i in range(self.count):
            print(self.array[i])


