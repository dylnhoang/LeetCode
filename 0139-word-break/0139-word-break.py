class Solution(object):
    def wordBreak(self, s, wordDict):

        #top-down DP approach, memoization

        dp = [False] * (len(s) + 1) #dp[i] = whether it is possible to create a valid word starting from s[i]
        dp[len(s)] = True #base case, if the end of the string is reached, it is possible to create a valid word starting from some index

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict: #check every word in wordDict to see if a word can be formed starting from index i 
                if ((i + len(w) <= len(s)) and (s[i : i + len(w)] in wordDict)):
                    dp[i] = dp[i + len(w)] #dp[i] is only possible if dp[i + len(w) is possible
                if dp[i]:
                    break #no need to continue going through words if a possible route to a valid word has been found from index i 
        
        return dp[0] #possible if possible from first index 
        