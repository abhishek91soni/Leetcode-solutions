# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collection import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if root is None:
            return
        maxwidth = 0
        q = deque([(root, 0)])
        while q:
            level_order = len(q)
            first_idx = q[0][1]
            last_idx = 0
            for _ in range(level_order):
                node, idx = q.popleft()
                idx -= first_idx
                last_idx = idx
                if node.left:
                    q.append((node.left, 2*idx))
                if node.right:
                    q.append((node.right, 2*idx+1))
            
            maxwidth = max(maxwidth, last_idx+1)
        return maxwidth