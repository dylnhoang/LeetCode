class Solution(object):
    def rob(self, nums):
        # sub-problem: what is the maximum amount of money you can extract from the last two houses?
        # thus, problem can be solved using bottom-up DP

        # max money two houses ago, max money one house ago 
        house2, house1 = 0, 0 # returns 0 if nums is empty

        for n in nums:
            current = max(n + house2, house1) # maximum amount you can get by house n
            house2 = house1 # iterate, the house that was two houses ago is now only one house ago
            house1 = current

        return house1 # loop ends after the final house, so the last house is one house ago