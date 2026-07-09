class Solution(object):
    def coinChange(self, coins, amount):
        # first thoughts are to use a greedy algo, but this won't work, because that's not how lin combs work
        # second thoughts are to go through every possible combination of coins in a tree-like fashion. of course, this is suboptimal, because its like n^A where n = len(coins) and A = amount
        # we notice that we're going to reach a different subamount multiple times on different combinations, turning this into a problem optimized through DP
        # thus, we propose a soln using bottom-up tabulation, where we tabulate the min comb of coins needed to get increasing amounts so we have them ready for use later

        # setting up the solution
        dp = [(amount + 1)] * (amount + 1) # most coins it can teach to make amount is (amount) b/c min value of a coin is 1
        dp[0] = 0 # base case: you need 0 coins to get 0 

        for a in range(1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    # logic is that you either already have the max, or you can get it from some different min comb of coins (+ 1 b/c you need the current coin c as well)
                    dp[a] = min(dp[a], 1 + dp[a - c]) 
        
        # if dp[amount] has changed then the line (16) above ran, and we can return a valid amount. otherwise, it's not possible to get amount from the coins and we return -1
        return dp[amount] if dp[amount] != (amount + 1) else -1 