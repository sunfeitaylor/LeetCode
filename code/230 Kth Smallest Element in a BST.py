# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nodes = []
        self.visitNode(root, nodes)
        return nodes[k - 1]

    def visitNode(self, root, nodes):
        if not root:
            return
        self.visitNode(root.left, nodes)
        nodes.append(root.val)
        self.visitNode(root.right, nodes)
