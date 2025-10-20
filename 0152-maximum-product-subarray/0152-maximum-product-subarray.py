class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Keep track of current min and max
        # Min is useful if next number is negative, bc then the greatest min will become the maximum value. 
        # Max is useful if next number is positive by same logic.
        # DP approach

        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            temp = curMin
            curMin = min(curMin * n, curMax * n, n)
            curMax = max(temp * n, curMax * n, n) # adding n as a potential current max/min handles a base case in which curMin = curMax and you'd choose n to be your respective min/max

            res = max(curMax, res)
        
        return res


