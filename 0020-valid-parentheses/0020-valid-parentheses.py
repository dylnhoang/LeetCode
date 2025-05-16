class Solution(object):
    def isValid(self, s):
        stack = []
        valid = {"}" : "{",
                 "]" : "[",
                 ")" : "("}
        for c in s:
            if c in valid:
                if not stack or stack.pop() != valid[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0