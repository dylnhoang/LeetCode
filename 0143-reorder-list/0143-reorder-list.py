# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        prev = slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        cur = head
        
        while cur and prev:
            temp1, temp2 = cur.next, prev.next
            cur.next = prev
            prev.next = temp1
            cur, prev = temp1, temp2