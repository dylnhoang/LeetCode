class Solution(object):
    def rob(self, nums):
        # same premise as house robber, but can't rob both first and last house
        # thus, we propose a soln in which we split the problem into two cases and choose the maximum
        #   either you rob the first house and not the last house, or rob the last house and not the first house
        #   can be done using a helper function that runs house robber 1 code

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) # nums[0] handles the edge case where there is only one house in nums

    def helper(self, nums):
        # see house robber for documentation
        house2, house1 = 0, 0

        for n in nums:
            cur = max(n + house2, house1)
            house2 = house1
            house1 = cur

        return house1
        