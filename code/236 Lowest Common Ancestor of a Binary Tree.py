# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        father_map = {root: None}
        self.dfs(root, father_map)
        father_p, father_q = p, q
        father_of_p = [p]
        while father_p:
            father_p = father_map[father_p]
            father_of_p.append(father_p)
        while father_q not in father_of_p:
            father_q = father_map[father_q]
        return father_q

    def dfs(self, node, father_map):
        if node:
            if node.left:
                father_map[node.left] = node
            if node.right:
                father_map[node.right] = node
            self.dfs(node.left, father_map)
            self.dfs(node.right, father_map)


class Solution:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.res

    def dfs(self, node, p, q):
        if not node:
            return False
        l = self.dfs(node.left, p, q)
        r = self.dfs(node.right, p, q)
        mask = node == p or node == q
        if l + r + mask >= 2:
            self.res = node
        return l or r or mask
