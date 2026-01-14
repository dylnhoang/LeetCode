class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curChars = set()
        res = 0

        for i in range(len(s)):
            while s[i] in curChars:
                curChars.remove((s[l]))
                l += 1
            
            curChars.add(s[i])
            r += 1
            curLen = r - l 
            res = max(res, curLen)
        
        return res