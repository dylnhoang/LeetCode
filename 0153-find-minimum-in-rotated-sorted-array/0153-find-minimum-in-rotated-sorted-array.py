class Solution(object):
    def findMin(self, nums):
        #sorted -- most likely a binary search algo
        #if nums[r] < nums[m], we know value lies to the right of index m. else, value is to the left OR is at index m

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
        