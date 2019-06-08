# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = - float('inf')
        self.maxsum(root)
        return self.max

    def maxsum(self, node):
        if not node:
            return 0
        left = self.maxsum(node.left)
        right = self.maxsum(node.right)
        self.max = max(self.max, node.val + left + right)
        return max(node.val + max(left, right), 0)
