class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two-pointer method: start two pointers at each end and shrink the base length (L) 
        # since you're shrinking L as you progress, you want to MAXIMIZE the height of the new rectangle (h)
        # so, at each step, progress only the pointer with the smaller h value as to maximize area

        # note: area = L * min(height1, height2), where L = r - l

        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            height1, height2 = height[l], height[r]
            area = (r - l) * min(height1, height2)

            maxArea = max(maxArea, area)

            if height1 < height2:
                l += 1
            else:
                r -= 1
            
        return maxArea

