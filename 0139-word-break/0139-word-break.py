class Solution(object):
    def wordBreak(self, s, wordDict):
        # idea: the validity of the string depends on the validity of the various substrings within it
        # so, we can use a top-down DP approach with memoization, caching whether it is possible to form a valid string at a certain point
        # we go backwards and mark whether it's possible to form a valid string at position i, because at i we need to know if the points at (i + 1) onward are valid
        #if we can get to the end from 0, we have a valid string

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # base case: if we reach the end of the string, we're done

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                cand = i + len(w)
                if cand <= len(s) and s[i : cand] in wordDict:
                    dp[i] = dp[cand] # if we can create a word at i, then the string is valid iff the we can create a different set of words at i + len(w)
                    print(dp[i : cand])
                    if dp[i]:
                        break # we only need to find one valid string at i

        return dp[0]


