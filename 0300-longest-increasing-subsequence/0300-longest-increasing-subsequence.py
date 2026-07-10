class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * (n + 1)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])

        return max(dp)
        