import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def reset(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        if new_capacity < 16: new_capacity = 16
        new_array = self.make_array(new_capacity)

        for i in range(min(self.count, new_capacity)):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    # def resize(self, new_capacity):
    #     if new_capacity < 16: new_capacity = 16
    #     new_array = self.make_array(new_capacity)
    #     for i in range(self.count):
    #         new_array[i] = self.array[i]
    #     self.array = new_array
    #     self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def shift_vals_from_i(self, i):
        cur_index = self.count
        while cur_index > i:
            self.array[cur_index] = self.array[cur_index-1]
            cur_index -= 1

    def shift_vals_to_i(self, i):
        cur_index = self.count - 1
        while cur_index > i:
            self.array[cur_index-1] = self.array[cur_index]
            cur_index -= 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Wrond index.')

        if self.count >= self.capacity:
            self.resize(self.capacity * 2)

        if i == self.count:
            self.array[i] = itm
            self.count += 1
            return

        if 0 <= i < self.count:
            self.shift_vals_from_i(i)
            self.array[i] = itm
            self.count += 1

        # if self.count == self.capacity:
        #     self.resize(self.capacity * 2)
        #     self.array[i] = itm

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Wrong index.')
        if self.count == 1:
            self.count = 0
            self.array[0] = None
            return

        self.shift_vals_to_i(i)
        self.count -= 1
        self.array[self.count] = None

        # Resize based on emptiness after deletion
        emptiness = self.capacity / (self.count - 1)
        if emptiness >= 1.5:
            self.resize(int(self.capacity / 1.5))

    # def delete(self, i):
    #     if i < 0 or i >= self.count:
    #         raise IndexError('Wrong index.')
    #     if self.count == 1:
    #         self.count = 0
    #         self.array[0] = None
    #         return
    #
    #     self.shift_vals_to_i(i)
    #     self.count -= 1
    #     self.array[self.count] = None
    #
    #     emptiness = self.capacity / self.count
    #     if emptiness >= 1.5:
    #         self.resize(int(self.capacity / 1.5))

    def list_vals(self):
        res = []
        for i in range(self.count):
            res.append(self.array[i])
        return res

    def print_vals(self):
        for i in range(self.count):
            print(self.array[i])

