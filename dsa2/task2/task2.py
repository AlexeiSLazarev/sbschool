from typing import List, Optional, Any


class SimpleTreeNode:
    def __init__(self, val: Any, parent: Optional['SimpleTreeNode'] = None):
        self.NodeValue = val
        self.Parent = parent
        self.Children: List['SimpleTreeNode'] = []
        self.level = 0


class SimpleTree:
    def __init__(self, root: Optional[SimpleTreeNode] = None):
        self.Root: Optional[SimpleTreeNode] = root
        self.set_levels()

    def AddChild(self, parent_node: SimpleTreeNode, new_child: SimpleTreeNode) -> None:
        if new_child.Parent:
            if new_child in new_child.Parent.Children:
                new_child.Parent.Children.remove(new_child)
        parent_node.Children.append(new_child)
        new_child.Parent = parent_node
        self.set_levels()

    def DeleteNode(self, node_to_delete: SimpleTreeNode) -> None:
        if node_to_delete == self.Root:
            self.Root = None
        elif node_to_delete.Parent:
            node_to_delete.Parent.Children.remove(node_to_delete)
            node_to_delete.Parent = None
        self.set_levels()

    def process_node(self, node: SimpleTreeNode) -> List[SimpleTreeNode]:
        nodes = [node]
        for child in node.Children:
            nodes.extend(self.process_node(child))
        return nodes

    def GetAllNodes(self) -> List[SimpleTreeNode]:
        if self.Root is None:
            return []
        return self.process_node(self.Root)


    def FindNodesByValue(self, val: Any) -> List[SimpleTreeNode]:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        return [node for node in node_list if node.NodeValue == val]

    def MoveNode(self, original_node: SimpleTreeNode, new_parent: SimpleTreeNode) -> None:
        if original_node == self.Root:
            return
        if original_node == new_parent or original_node in new_parent.Children:
            return

        if original_node.Parent:
            original_node.Parent.Children.remove(original_node)
        new_parent.Children.append(original_node)
        original_node.Parent = new_parent
        self.set_levels()

    def Count(self) -> int:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        return len(node_list)

    def LeafCount(self) -> int:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        num_leaf = [node for node in node_list if len(node.Children) == 0]
        return len(num_leaf)

    def set_node_level(self, node: SimpleTreeNode, level: int) -> None:
        node.level = level
        for child in node.Children:
            self.set_node_level(child, level + 1)

    def set_levels(self) -> None:
        if self.Root is not None:
            self.set_node_level(self.Root, 0)
