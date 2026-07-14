class Solution(object):
    def lengthOfLIS(self, nums):
        LIS = [1] * (len(nums) + 1)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)