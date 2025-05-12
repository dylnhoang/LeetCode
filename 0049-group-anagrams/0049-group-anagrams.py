class Solution(object):
    def groupAnagrams(self, strs):
        str_hash = defaultdict(list)

        for s in strs:
            alph_hash = [0] * 26
            for c in s:
                alph_hash[ord(c)-ord('a')] += 1
            str_hash[tuple(alph_hash)].append(s)
        
        return list(str_hash.values())
        

        