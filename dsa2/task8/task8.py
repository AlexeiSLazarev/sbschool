from typing import List, Optional


class Heap:

    def __init__(self):
        self.HeapArray: List[Optional[int]] = []
        self.depth: int = 0
        self.tree_size: int = 0
        self.root: int = 0
        self.num_elements: int = 0

    def MakeHeap(self, input_array: List[int], depth: int) -> None:
        self.depth = depth
        self.tree_size = 2 ** (self.depth + 1) - 1
        self.HeapArray = [None] * self.tree_size  # Array of keys
        self.root = 0
        for key in input_array:
            self.Add(key)

    def Add(self, key: int) -> bool:
        if self.num_elements >= self.tree_size:
            return False
        if self.num_elements == 0:
            self.HeapArray[0] = key
            self.num_elements += 1
            return True
        self.HeapArray[self.num_elements] = key
        self.num_elements += 1
        self.move_up_element(self.num_elements - 1)
        return True

    def is_parent_less(self, current_key: int) -> bool:
        parent_key = self.get_parent(current_key)
        if parent_key < 0:
            return False
        parent_val = self.HeapArray[parent_key]
        current_val = self.HeapArray[current_key]
        if parent_val is not None and current_val is not None and parent_val < current_val:
            return True
        return False

    def move_up_element(self, current_key: int) -> None:
        if current_key <= 0:
            return
        parent_key = self.get_parent(current_key)
        if self.is_parent_less(current_key):
            self.HeapArray[current_key], self.HeapArray[parent_key] = self.HeapArray[parent_key], self.HeapArray[
                current_key]
            self.move_up_element(parent_key)

    def get_parent(self, node_key: int) -> int:
        return (node_key - 1) // 2

    def get_left_child(self, node_key: int) -> int:
        return 2 * node_key + 1

    def get_right_child(self, node_key: int) -> int:
        return 2 * node_key + 2

    def GetMax(self) -> int:
        if self.num_elements == 0:
            return -1
        max_element = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.num_elements - 1]
        self.HeapArray[self.num_elements - 1] = None
        self.num_elements -= 1
        self.heapify_root_element(0)
        return max_element

    def heapify_root_element(self, current_key: int) -> None:
        largest = current_key
        left = self.get_left_child(current_key)
        right = self.get_right_child(current_key)

        if left < self.num_elements and self.HeapArray[left] is not None and self.HeapArray[left] > self.HeapArray[
            largest]:
            largest = left

        if right < self.num_elements and self.HeapArray[right] is not None and self.HeapArray[right] > self.HeapArray[
            largest]:
            largest = right

        if largest != current_key:
            self.HeapArray[current_key], self.HeapArray[largest] = self.HeapArray[largest], self.HeapArray[current_key]
            self.heapify_root_element(largest)

    def get_tree_list(self) -> List[Optional[int]]:
        return self.HeapArray

    def print_tree(self) -> None:
        print("*" * 20)
        self.print_tree_recursive(0)
        print("*" * 20)

    def print_tree_recursive(self, node_index: int, level: int = 0) -> None:
        if node_index >= self.tree_size:
            return
        self.print_tree_recursive(self.get_left_child(node_index), level + 1)
        if self.HeapArray[node_index] is not None:
            print(' ' * 4 * level + '-> ' + str(self.HeapArray[node_index]))
        self.print_tree_recursive(self.get_right_child(node_index), level + 1)
