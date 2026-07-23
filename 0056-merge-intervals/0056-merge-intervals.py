class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # we start by sorting the array of intervals to make collision detection easier 
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]
        # res[-1] will represent the current interval we are checking for collision to determine if we want to merge

        for i in range(1, len(intervals)):
            curInterval = intervals[i]

            # condition for merging: if the curInterval starts before res[-1] ends (inclusively)
            # this is the only condition because we sorted the array by start time 

            if curInterval[0] <= res[-1][1]:
                # merge
                res[-1] = [res[-1][0], max(res[-1][1], curInterval[1])]
            else:
                res.append(curInterval)

        return res

        # we now only have to worry about end values and can handle things sequentially 
        