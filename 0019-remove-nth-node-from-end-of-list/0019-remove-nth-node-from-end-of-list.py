# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if size == n:
            return head.next
        res = size - n
        temp = head
        while temp:
            res -= 1
            if res == 0:
                break
            temp = temp.next
        temp.next = temp.next.next
        return head
