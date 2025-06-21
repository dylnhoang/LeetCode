class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(open, close):
            if close == open == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

        #Notes
        #Stack used b/c of easy popping
        #Recursion hinted b/c we are trying to find all combinations of something
        #Thinking
        