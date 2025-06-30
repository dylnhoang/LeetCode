class Solution(object):
    def findLHS(self, nums):
        numsMap = {}
        res = 0

        for n in nums:
            numsMap[n] = 1 + numsMap.get(n, 0)
        
        for key, value in numsMap.items():
            if numsMap.get(key + 1):
                length = numsMap[key + 1] + value
                res = max(res, length)
        
        return res