# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return
        q = deque([(root, 0,0)])
        mp = {}
        while q:
            node, row, col = q.popleft()
            if col not in mp:
                mp[col]= []
            mp[col].append((row, node.val))
            if node.left:
                q.append((node.left, row+1, col-1))
            if node.right:
                q.append((node.right, row+1, col+1))
        arr = []
        for col in sorted(mp):
            mp[col].sort()
            level = []
            for row, value in mp[col]:
                level.append(value)
            arr.append(level)
        return arr
