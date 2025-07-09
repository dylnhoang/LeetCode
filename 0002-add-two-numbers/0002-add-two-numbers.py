# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_num = 0
        l2_num = 0

        l1_factor = 1
        l2_factor = 1

        while l1:
            l1_num += l1.val * l1_factor
            l1_factor *= 10
            l1 = l1.next

        while l2:
            l2_num += l2.val * l2_factor
            l2_factor *= 10
            l2 = l2.next
        
        num = l1_num + l2_num

        cur = ListNode()
        dummy = cur

        if num == 0:
            return ListNode(0)

        while num != 0:
            cur.next = ListNode(num%10)
            num //= 10
            cur = cur.next
        
        return dummy.next


