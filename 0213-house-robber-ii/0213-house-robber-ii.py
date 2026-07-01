class Solution(object):
    def rob(self, nums):
        # you can either take the maximum of the houses without the first or without the last, but you cannot include both because they are linked
        # thus, we propose a soln in which you create a helper function and run it on a portion of the array without the last house, and on a portion of the array without the first house

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        house2, house1 = 0, 0 # max 2 houses ago, max 1 house ago

        for n in nums:
            # calculate current max value
            current = max(n + house2, house1)
            house2, house1 = house1, current
                
        return house1

            