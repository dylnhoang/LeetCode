class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom-up DP: tabulation
        # the key idea is that the minimum amount of coins needed to make (amount) is the minimum amount 
        # to make (amount-coin) for some coin and adding 1 to that amount

        # thus, we can get a good solution by checking each combination of coins, and optimize this solution by caching the minimum amount of coins it takes to make some number, which will be revisited across different combinations

        dp = [(amount + 1)] * (amount + 1) # the max coins it can take to create amount is amount (b/c the minimum coin value is 1)
        dp[0] = 0 # base case: it takes 0 coins to make 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # either you HAVE the optimal amount, or you can create a new one by choosing a different combination of coins
                    dp[a] = min(dp[a], 1 + dp[a - c]) 
        
        return dp[amount] if dp[amount] != (amount + 1) else -1 # if dp[amount] == amount + 1 they're no way to reach that value