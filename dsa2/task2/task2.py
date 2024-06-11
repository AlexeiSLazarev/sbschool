from typing import List, Optional, Any


class SimpleTreeNode:
    def __init__(self, val: Any, parent: Optional['SimpleTreeNode'] = None):
        self.node_value = val
        self.parent = parent
        self.children: List['SimpleTreeNode'] = []
        self.level = 0


class SimpleTree:
    def __init__(self, root: Optional[SimpleTreeNode] = None):
        self.root: Optional[SimpleTreeNode] = root
        self.set_levels()

    def AddChild(self, parent_node: SimpleTreeNode, new_child: SimpleTreeNode) -> None:
        if new_child.parent:
            if new_child in new_child.parent.children:
                new_child.parent.children.remove(new_child)
        parent_node.children.append(new_child)
        new_child.parent = parent_node
        self.set_levels()

    def DeleteNode(self, node_to_delete: SimpleTreeNode) -> None:
        if node_to_delete == self.root:
            self.root = None
        elif node_to_delete.parent:
            node_to_delete.parent.children.remove(node_to_delete)
            node_to_delete.parent = None
        self.set_levels()  # обновляем уровни узлов

    def process_node(self, node_list: List[SimpleTreeNode], node_index: int, node_values: List[SimpleTreeNode]) -> None:
        if node_index < 0:
            return
        current_node: SimpleTreeNode = node_list[node_index]
        node_values.append(current_node)
        num_children: int = len(current_node.children)
        if num_children > 0:
            self.process_node(current_node.children, num_children - 1, node_values)
        self.process_node(node_list, node_index - 1, node_values)

    def GetAllNodes(self) -> List[SimpleTreeNode]:
        if self.root is None:
            return []
        if len(self.root.children) == 0:
            return [self.root]
        node_list: List[SimpleTreeNode] = self.root.children
        node_index: int = len(node_list) - 1
        node_values: List[SimpleTreeNode] = [self.root]
        self.process_node(node_list, node_index, node_values)
        return node_values

    def search_node_by_value(self, node_list: List[SimpleTreeNode], node_index: int, value: int) -> List[SimpleTreeNode]:
        if node_index < 0:
            return []
        if node_list[node_index].node_value == value:
            return [node_list[node_index]] + self.search_node_by_value(node_list, node_index - 1, value)
        return self.search_node_by_value(node_list, node_index - 1, value)

    def FindNodesByValue(self, val: Any) -> List[SimpleTreeNode]:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        return self.search_node_by_value(node_list, len(node_list) - 1, val)

    def MoveNode(self, original_node: SimpleTreeNode, new_parent: SimpleTreeNode) -> None:
        if original_node == self.root:
            return
        self.DeleteNode(original_node)
        self.AddChild(new_parent, original_node)
        self.set_levels()

    def Count(self) -> int:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        return len(node_list)

    def LeafCount(self) -> int:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        num_leaf = [node for node in node_list if len(node.children) == 0]
        return len(num_leaf)

    def set_node_level(self, node: SimpleTreeNode, level: int) -> None:
        node.level = level
        for child in node.children:
            self.set_node_level(child, level + 1)

    def set_levels(self) -> None:
        if self.root is not None:
            self.set_node_level(self.root, 0)
