class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom-up DP
        # ways(n) = ways(n - 1) + ways(n - 2)

        one, two = 1, 1 # init

        for i in range(n - 1):
            one, two = one + two, one # step

        return one