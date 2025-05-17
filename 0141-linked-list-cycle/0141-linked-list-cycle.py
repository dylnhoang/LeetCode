# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        node_set = set()
        cur = head
        while cur:
            if cur in node_set:
                return True
            node_set.add(cur)
            cur = cur.next
        return False
        