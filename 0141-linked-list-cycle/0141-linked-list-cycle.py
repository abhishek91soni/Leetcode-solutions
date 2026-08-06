# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        curr = head
        while(curr is not None):
            if curr in hashmap:
                print(hashmap)
                return True
            hashmap[curr] = 1
            curr = curr.next
        return False