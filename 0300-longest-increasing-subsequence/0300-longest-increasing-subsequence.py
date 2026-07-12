class Solution(object):
    def lengthOfLIS(self, nums):
        # idea: the LIS at point i in the list is determined by the LIS at point j (where nums[j] is a value greater than nums[i], WLOG)
        # brute-force idea would be to use recursion, but this would be a O(2^n) soln; clearly not optimal
        # we can optimize using a top-down DP approach, where we memoize the LIS at point i for later usage at point (i - 1) WLOG

        LIS = [1] * (len(nums) + 1)
        
        for i in range(len(nums) - 1, -1, -1): # go backwards through nums
            for j in range(i + 1, len(nums)): # check every value in front of nums[i]
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j]) # either the stored value is already the max, or we can form a better LIS at point i by prepending to a LIS at point j

        return max(LIS)

        
