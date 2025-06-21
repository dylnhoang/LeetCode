class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        Notes
        Add INDICES of temperatures to a stack (Allows for us to understand the corresponding index position in res later)
        Before adding, check if new temperature (at index) is greater than old temperatures (by indices).
        While it is, pop these values and add the difference in their indices to their corresponding index position in res.
        At the end of iteration through temperatures, unpopped temperatures will have their corresponding indices in res set to
        zero.
        """

        stack = [] #Holds indices of temperatures
        res = [0] * len(temperatures) #Holds differences in indices

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and temperatures[stack[-1]] < temp:
                res[stack[-1]] = (i - stack[-1])
                stack.pop()
            stack.append(i)
        
        return res



        