class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 #rob1 stores max loot two houses ago, rob2 stores max loot one house ago
        for n in nums:
            temp = max(n + rob1, rob2) #either steal from this house or check the other path
            rob1 = rob2 #move houses
            rob2 = temp 
        return rob2 #rob2 will be the full max at the end