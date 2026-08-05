class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0]) # sort intervals by ascending start
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # non-overlapping
            if start >= prevEnd:
                prevEnd = end
            # overlapping
            else:
                res += 1
                prevEnd = min(end, prevEnd) # idea: keeping the point with the earlier end-time is optimal b/c it leaves more room for later intervals to fill (think about number lines)
            
        return res