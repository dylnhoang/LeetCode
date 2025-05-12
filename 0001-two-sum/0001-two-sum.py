class Solution(object):
    def twoSum(self, nums, target):
        numHash = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numHash:
                return [numHash[diff], i]
            numHash[n] = i
        