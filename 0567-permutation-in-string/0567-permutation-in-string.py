class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1_hash = [0] * 26
        s2_hash = [0] * 26
        
        #Populate s1_hash
        for i in range(len(s1)):
            s1_hash[ord(s1[i]) - ord('a')] += 1
            s2_hash[ord(s2[i])- ord('a')] += 1
        
        for j in range(len(s1), len(s2)):
            if s1_hash == s2_hash:
                return True
            
            s2_hash[ord(s2[j - len(s1)]) - ord('a')] -= 1
            s2_hash[ord(s2[j]) - ord('a')] += 1

        return s1_hash == s2_hash

