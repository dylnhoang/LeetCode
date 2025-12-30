class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 # max money 1 house ago, max money 2 houses ago

        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2) # advancing; either decide to rob this house or forgo b/c the profits of robbing the house between them is larger
        
        return rob2