class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            time = 0
            for p in piles:
                time += ceil(float(p)/k)
            if time <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
            
        