class Solution(object):
    def wordBreak(self, s, wordDict):
        # idea: the validity of a word is defined by the validity of the following string
        # i.e. we should start from the end of the string to check for words first, because if we can't find words at the end of the string, there's no words in the beginning

        dp = [False] * (len(s) + 1) 
        dp[len(s)] = True # if we reach the end of the string (from the beginning), we know we our string is valid

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] in wordDict:
                    dp[i] = dp[i + len(w)] # refer to idea
                    if dp[i]:
                        break
        
        return dp[0]
        