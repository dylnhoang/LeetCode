class Solution(object):
    def carFleet(self, target, position, speed):
        #Idea: Cars can only catch up to, but not pass, cars in front of them
        #Execution: Order cars by decreasing position. If the time it takes for a car behind it to reach target is less than     
        #           or equal to a car in front of it, they form a fleet.
        #Formula: time = (target - position) / speed
        #Data Structure: Using a stack, but could also do problem through simple iteration.
        #Time Complexity: O(nlogn), because although each node is visited once, sorting is nlogn. 
        #Space Complexity: O(n), because potentially creating a stack with every value if no fleets form. 

        stack = []

        pairs = list(zip(position, speed))
        pairs.sort(reverse = True)
        
        for p, s in pairs:
            stack.append((target - p) * 1.0 / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

