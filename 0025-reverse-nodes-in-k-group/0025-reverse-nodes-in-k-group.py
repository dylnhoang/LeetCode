# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)

            if not kth:
                break
            
            #start of next group
            groupNext = kth.next

            #reversing
            prev, cur = groupNext, groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            #setting next groups
            temp = groupPrev.next #groupPrev.next is originally the beginning of group, now is technically end of rearranged group
            groupPrev.next = kth #kth originally at end of group, now connected to end of last group and is beginning of rearranged group
            groupPrev = temp #keep reference to new 'dummy' node that is before new group of interest

        return dummy.next

    #helper method
    def getKth(self, cur, k):
        while cur and k > 0:
            k -= 1
            cur = cur.next
        return cur
        