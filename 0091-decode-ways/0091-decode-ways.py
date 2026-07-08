class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom-up DP: the number of decodings at position i are the number of decodings at position (i + 1) and position (i + 2)

        dp = {len(s) : 1} # there is only one way to decode the last letter of the string

        def dfs(i):
            if i in dp:
                return dp[i] # base case 1: we've already explored this possibility (caching for efficiency)
            if s[i] == "0":
                return 0 #there's no way to decode a string starting with 0 
            
            res = dfs(i + 1)
            if (i + 1) < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)

        
