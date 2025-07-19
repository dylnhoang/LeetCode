"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        oldToCopy = { None : None }
        
        #first pass (populating map)
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next
        
        #second pass (adding pointers)
        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]
        