class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        # idea: once you find a common char between the two strings at index i, j, we have a SUBPROBLEM (-> DP) of finding the LCS between the strings from index (i + 1) and index (j + 1)
        # we can utilize 2D DP to apply this idea; we create a grid where grid[i][j] represents the length of the LCS between text1[i:] and text2[j:]
        # if we find a common character at i, j, we can say that grid[i][j] = 1 + grid[i + 1][j + 1]
        # else, we look at the LCS at [i + 1][j] and [i][j + 1] and let grid[i][j] be the maximum of those two
        # these results need to be computed beforehand, so we work backwards knowing that the base-case is at the end of either string, where the LCS is 0

        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)] # dp[x][y] = the LCS btwn text2[x:] and text1[y:]

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
        