class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        res = 0

        for n in num_set:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1 
                
                res = max(res, length)

        return res

        