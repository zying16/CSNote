# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        stack = [(root, root.val)]

        while stack:
            (node, total) = stack.pop()
            if node.left:
                stack.append((node.left, total + node.left.val))
            if node.right:
                stack.append((node.right, total + node.right.val))
            if not node.left and not node.right and total == sum:
                return True
        return False
