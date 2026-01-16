class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two-pointer method: start l and r at opposite ends and move pointer that points to the lower height
        # works b/c area = l * h, and l is always going to get smaller, so h is the thing we must up to up area

        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            leftHeight, rightHeight = height[l], height[r]

            area = min(leftHeight, rightHeight) * (r - l)
            maxArea = max(area, maxArea)

            if leftHeight < rightHeight:
                l += 1
            else:
                r -= 1
        
        return maxArea