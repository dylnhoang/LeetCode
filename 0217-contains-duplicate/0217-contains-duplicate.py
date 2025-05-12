class Solution(object):
    def containsDuplicate(self, nums):
        numSet = set()
        for i, n in enumerate(nums):
            if n in numSet:
                return True
            else:
                numSet.add(n)
        
        return False

        