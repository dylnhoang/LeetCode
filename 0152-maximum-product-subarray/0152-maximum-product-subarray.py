class Solution(object):
    def maxProduct(self, nums):
        # this is a DP problem because if we know the previous maximum at a certain point, we know the current maximum at that point
        # however, we also need to keep track of the previous minimum b/c there are negative numbers involved
        # bottom-up DP: max subarray at i depends on max subbaray at (i - 1)

        res = max(nums) # just some filler value for res (can't be 0 b/c max could be negative)
        curMin, curMax = 1, 1

        for n in nums:
            temp = curMax
            # need to include n because curMin and curMax may both be negative at some point, think [-1, 8]
            curMax = max(curMin * n, curMax * n, n) 
            curMin = min(curMin * n, temp * n, n)
            res = max(res, curMax)
        
        return res

        