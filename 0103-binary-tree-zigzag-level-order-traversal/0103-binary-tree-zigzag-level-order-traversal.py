# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collection import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        arr = []
        if root is None:
            return arr
        q = deque([root])
        flag = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag == 0:
                left = []
                for x in level:
                    left.append(x)
                arr.append(left)
                flag = 1
            else:
                right = []
                for x in level[::-1]:
                    right.append(x)
                arr.append(right)
                flag = 0
        return arr
            
                