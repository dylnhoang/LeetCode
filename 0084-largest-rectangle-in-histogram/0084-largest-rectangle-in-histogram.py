class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = (i - index) * height
                maxArea = max(maxArea, area)
                start = index
            stack.append([start, h])

        #iterate through unpopped items after initial iteration
        while stack:
            index, height = stack.pop()
            i = len(heights)
            area = (i - index) * height
            maxArea = max(maxArea, area)

        return maxArea