# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        new_head = self.reverse_linkedlist(slow.next)
        first = head
        second = new_head
        while second:
            if(first.val != second.val):
                self.reverse_linkedlist(new_head)
                return False
            second = second.next
            first = first.next
        self.reverse_linkedlist(new_head)
        return True

    def reverse_linkedlist(self,head):
        prev = None
        curr = head
        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

