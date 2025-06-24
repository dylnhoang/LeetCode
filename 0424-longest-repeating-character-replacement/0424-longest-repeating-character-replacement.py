class Solution(object):
    def characterReplacement(self, s, k):
        i = 0
        res = 0
        freq = [0] * 26
        maxf = 0

        for j in range(len(s)):
            freq[ord(s[j]) - ord('A')] += 1
            maxf = max(freq[ord(s[j]) - ord('A')], maxf)
            
            while j - i + 1 - maxf > k:
                freq[ord(s[i]) - ord('A')] -= 1
                i += 1
            
            res = max(res, j - i + 1)
        
        return res
