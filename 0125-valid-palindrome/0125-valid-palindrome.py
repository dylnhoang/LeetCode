class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1 
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True