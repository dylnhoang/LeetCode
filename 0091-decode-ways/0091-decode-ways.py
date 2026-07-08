class Solution(object):
    def numDecodings(self, s):
        # bottom-up DP: the decodings at position i depend only on the decodings of position (i + 1) and the decodings of position (i + 2)

        dp = {len(s): 1} #there is one way to decode the last digit of the string

        def dfs(i):
            if i in dp:
                return dp[i] # base case 1: we've already cached i in dp and do not need to compute further
            if s[i] == "0":
                return 0 # base case 2: we cannot decode a string starting with 0 (i is the assumed starting position of some substring)
            
            # since we know the string doesn't start in zero, we know we can at least have a string starting with the char at position i 
            res = dfs(i + 1) # all decodings at position (i + 1) starting with s[i]

            # if 10 < s[i : i + 2] < 26, we can also add decodings from position (i + 2) starting with s[i : i + 2]
            if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")): 
                res += dfs(i + 2)

            dp[i] = res # cache for optimization
            return res

        return dfs(0)

        