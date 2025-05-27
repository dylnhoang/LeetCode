class Solution(object):
    def checkInclusion(self, s1, s2):
        size = len(s1)

        if size > len(s2):
            return False
        
        s1_hash = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}

        for c in s1:
            s1_hash[c] += 1

        for i in range(len(s2)-size + 1):
            s2_hash = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
            for c in s2[i : i + size]:
                s2_hash[c] += 1
            if s2_hash == s1_hash:
                return True
        
        return False
        