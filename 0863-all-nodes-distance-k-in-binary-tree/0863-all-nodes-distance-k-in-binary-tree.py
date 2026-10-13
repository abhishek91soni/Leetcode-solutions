# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []
        parent = {}
        def parents(node, par = None):
            if node is None:
                return
            parent[node] = par
            parents(node.left, node)
            parents(node.right,node)
        parents(root)
        q = deque([(target,0)])
        visited = {target}
        while q:
            node, dist = q.popleft()
            if dist == k:
                return [node.val]+ [other.val for other , d in q if d == k]
            for neighbour in (node.left, node.right, parent[node]):
                if neighbour and neighbour not in visited:
                    visited.add(neighbour)
                    q.append((neighbour, dist+1))
        return []