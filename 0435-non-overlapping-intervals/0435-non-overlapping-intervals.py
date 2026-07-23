class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        # we start by sorting the array of intervals so that we can handle them sequentially
        # this also means there is only one condition for overlap: when a further interval starts before a previous one ends

        intervals.sort(key = lambda x: x[0])

        # thinking about this, if we want to remove an interval when there's a collision, is it better to remove the one with the later or earlier end point?
        # it will always be better to remove the one with the later end point, as this leaves a greater range of possibilities for start points that the rest of the intervals can have, i.e. minimizing removals
        # thus, the start point is irrelevant to this problem; we can just look at the end points of each interval and solve this problem efficiently 

        # so, we do this problem by keeping track of the previous endpoint, and changing this as we progress
        # if there's a collision, we change prevEnd to the min endpoint between the two colliding intervals

        count = 0
        prevEnd = intervals[0][1]


        for i in range(1, len(intervals)):
            curInterval = intervals[i]

            # check for collision, i.e. check if the current intervals starts before prevEnd
            if curInterval[0] < prevEnd:
                prevEnd = min(prevEnd, curInterval[1])
                count += 1
            else:
                prevEnd = curInterval[1]

        return count
