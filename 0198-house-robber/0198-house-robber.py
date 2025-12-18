class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 #rob1 stores max loot two houses ago, rob2 stores max loot one house ago
        
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)

        return rob2