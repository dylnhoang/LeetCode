class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        return s1_count == s2_count