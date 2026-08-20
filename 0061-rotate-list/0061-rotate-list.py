# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        tail = head
        size = 1
        while tail.next :
            tail = tail.next
            size += 1
        tail.next = head
        k = k % size
        steptoNewTail = size - k 
        newtail = head
        for _ in range(steptoNewTail - 1):
            newtail = newtail.next

        New_head = newtail.next
        newtail.next = None
        return New_head
