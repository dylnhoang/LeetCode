class Solution(object):
    def climbStairs(self, n):
        #top-down dp, number of ways to get to step i is number of ways to get to step (i-1) + number of ways to get to step (i-2)

        step1 = 1 
        step2 = 1

        for i in range(n):
            step1, step2 = step2, step2 + step1

        return step1
