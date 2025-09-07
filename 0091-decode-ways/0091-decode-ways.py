class Solution:
    def numDecodings(self, s: str) -> int:
        #bottom-up dp

        prevOne = 1 #one step ago, base case
        prevTwo = 0 #two steps ago

        for i in range(len(s)):
            cur = 0
            #if current number can be part of a valid double digit
            if i != 0 and s[i - 1 : i + 1] <= "26" and s[i - 1 : i + 1] >= "10": 
                cur = prevTwo
            if s[i] != "0": 
                cur += prevOne

            #step up
            prevTwo = prevOne 
            prevOne = cur
        
        return prevOne
