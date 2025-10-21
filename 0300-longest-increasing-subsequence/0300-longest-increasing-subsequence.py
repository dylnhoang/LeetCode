class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums) #LIS[i] = the length of the longest increasing subsequence starting from index i of nums

        #top-down DP approach: memoization
        #iterate i backwards, start j from i + 1 and iterate forwards
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                #if nums[j] is bigger than nums[i], you have found an increasing subsequence
                #thus we check if the length of the found subsequence (1 + LIS[j]) is larger or smaller than the current LIS[i] value
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)