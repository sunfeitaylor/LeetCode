# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while True:
            if q.val < root.val:
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:
                return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        return self.findAncestor(root, p, q)

    def findAncestor(self, root, p, q):
        if q.val < root.val:
            return self.findAncestor(root.left, p, q)
        elif p.val > root.val:
            return self.findAncestor(root.right, p, q)
        else:
            return root
