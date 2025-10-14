class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if (a-c) >= 0: #if a combination with the current coin and amount is possible
                    dp[a] = min(dp[a], 1 + dp[a - c]) #either current value, or coin + dp[amount]

        return dp[amount] if dp[amount] != float('inf') else -1
