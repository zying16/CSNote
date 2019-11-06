from _23_binary_tree import pre_order, in_order, post_order

class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root=None):
        self._root = root

    def find(self, value: int) -> TreeNode:
        node = self._root
        while node and node.val != value:
            node = node.left if value < node.val else node.right
        return node
        '''
        while node:
            if value == node.val:
                return node
            elif value > node.val:
                node = node.right
            else:
                node = node.left
        return None
        '''


    def insert(self, value: int):
        node_to_insert = TreeNode(value)
        if self._root is None:
            self._root = node_to_insert
            return 
        node = self._root
        while node:
            if value > node.val:
                if node.right is None:
                    node.right = node_to_insert
                    return
                node = node.right
            else:
                if node.left is None:
                    node.left = node_to_insert
                    return
                node = node.left

    def delete(self, value: int):
        node = self._root
        parent = None
        while node and node.val != value:
            parent = node
            node = node.left if node.val > value else node.right
        # not found
        if node is None:
            return
        # 要删除的节点有两个节点
        # 找到右子树最小的节点并替换掉要删除的节点
        if node.left and node.right:
            succesor_parent, succesor = node, node.right
            while succesor.left:
                succesor_parent, succesor = succesor, succesor.left
            # 替换数据
            node.val = succesor.val
            # 接下来变成删除 succesor
            parent, node = succesor_parent, succesor

        # 要删除的节点最多只有一个子节点
        child = node.left if node.left else node.right
        # 要删除的是根节点
        if parent is None:
            self._root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child




if __name__ == '__main__':
    root = TreeNode(33)
    b = BinarySearchTree(root)
    assert root == b.find(33)
    b.insert(17)
    assert root.left.val == 17
    b.insert(13)
    b.insert(16)
    b.insert(18)
    b.insert(50)
    b.insert(34)
    b.insert(58)
    assert list(pre_order(root)) == [33, 17, 13, 16, 18, 50, 34, 58]
    b.delete(16)
    assert list(pre_order(root)) == [33, 17, 13, 18, 50, 34, 58]
    b.delete(70)
    assert list(pre_order(root)) == [33, 17, 13, 18, 50, 34, 58]
    b.delete(17)
    assert list(pre_order(root)) == [33, 18, 13, 50, 34, 58]
    b.delete(33)
    assert list(pre_order(root)) == [34, 18, 13, 50, 58]
