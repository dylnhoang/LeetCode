# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Goals
        # 1. find 2nd half                 
        # 2. reverse 2nd half
        # 3. break link between the halves
        # 4. insert nodes in order

        # Methods
        # 1. use fast-slow pointer method
        # 2. reverse iteration algo
        # 3. ???
        # 4. iterate

        # 1.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. / 3.

        cur = slow.next
        prev = slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # 4.
        cur = head
        
        while prev and cur:
            temp1, temp2 = cur.next, prev.next
            cur.next = prev
            prev.next = temp1 
            cur, prev = temp1, temp2



        