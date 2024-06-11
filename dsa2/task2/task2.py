from typing import List, Any


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.node_value = val  # значение в узле
        self.parent = parent  # родитель или None для корня
        self.children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.root:SimpleTreeNode = root  # корень, может быть None

    def AddChild(self, parent_node: SimpleTreeNode, new_child: SimpleTreeNode):
        parent_node.children.append(new_child)
        new_child.parent = parent_node

    def DeleteNode(self, node_to_delete: SimpleTreeNode):
        if node_to_delete == self.root:
            self.root = SimpleTreeNode(1, None)
        parent: SimpleTreeNode = node_to_delete.parent
        parent.children.remove(node_to_delete)
        node_to_delete.parent = None

    def process_node(self, node_list: List[Any], node_index: int, node_values: List[Any]):
        if node_index < 0:
            return
        current_node: SimpleTreeNode = node_list[node_index]
        node_values.append(current_node)
        num_children: int = len(current_node.children)
        if num_children > 0:
            self.process_node(current_node.children, num_children - 1, node_values)
        self.process_node(node_list, node_index - 1, node_values)

    def GetAllNodes(self):
        if len(self.root.children) == 0:
            return []
        node_list: List[Any] = self.root.children
        node_index: int = len(node_list) - 1
        node_values: List[Any] = [self.root]
        self.process_node(node_list, node_index, node_values)
        return node_values

    def search_node_by_value(self, node_list: List[SimpleTreeNode], node_index: int, value: int):
        if node_index < 0:
            return []
        if node_list[node_index].node_value == value:
            return [node_list[node_index]] + self.search_node_by_value(node_list, node_index - 1, value)
        return self.search_node_by_value(node_list, node_index - 1, value)

    def FindNodesByValue(self, val):
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        return self.search_node_by_value(node_list, len(node_list)-1, val)

    def MoveNode(self, original_node: SimpleTreeNode, new_parent: SimpleTreeNode):
        self.DeleteNode(original_node)
        self.AddChild(new_parent, original_node)

    def Count(self):
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        return len(node_list)

    def LeafCount(self):
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        num_leaf = [node for node in node_list if len(node.children) == 0]
        return len(num_leaf)
