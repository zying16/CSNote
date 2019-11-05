class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None

# 前序遍历
def pre_order(node:TreeNode):
    if node:
        yield node.val
        yield from pre_order(node.left)
        yield from pre_order(node.right)

# 中序遍历
def in_order(node:TreeNode):
    if node:
        yield from in_order(node.left)
        yield node.val
        yield from in_order(node.right)


# 后序遍历
def post_order(node:TreeNode):
    if node:
        yield from post_order(node.left)
        yield from post_order(node.right)
        yield node.val


if __name__ == '__main__':
    '''
       1
     2  3
    4  5 6
    '''
    root = TreeNode(1)
    left1 = TreeNode(2)
    root.left = left1
    right1 = TreeNode(3)
    root.right = right1
    left2 = TreeNode(4)
    left1.left = left2
    right2 = TreeNode(5)
    right1.left = right2
    right3 = TreeNode(6)
    right1.right = right3
    assert list(pre_order(root)) == [1, 2, 4, 3, 5, 6]
    assert list(in_order(root)) == [4, 2, 1, 5, 3, 6]
    assert list(post_order(root)) == [4, 2, 5, 6, 3, 1]
