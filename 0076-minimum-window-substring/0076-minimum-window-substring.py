class Solution(object):
    def minWindow(self, s, t):
        t_map, window = {}, {}
        res, resLen = [-1, -1], float('inf')
        
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        have, need = 0, len(t_map)
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in t_map and window[c] == t_map[c]:
                have += 1
            
            while have == need:
                length = (r - l + 1)
                if length < resLen:
                    res = [l, r]
                    resLen = length

                left = s[l]
                window[left] -= 1

                if left in t_map and window[left] < t_map[left]:
                    have -= 1
                
                l += 1
            
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""

        

        