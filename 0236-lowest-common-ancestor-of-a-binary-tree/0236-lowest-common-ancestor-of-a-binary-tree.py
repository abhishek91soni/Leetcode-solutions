# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathp = []
        pathq = []
        def findPath(node, target, path):
            if node is None:
                return False

            if node == target:
                path.append(node)
                return True

            if findPath(node.left, target, path) or findPath(node.right, target, path):
                path.append(node)
                return True

            return False

        findPath(root, p, pathp)
        findPath(root, q, pathq)

        i = len(pathp) - 1
        j = len(pathq) - 1

        while i >= 0 and j >= 0 and pathp[i] == pathq[j]:
            i -= 1
            j -= 1

        return pathp[i + 1]