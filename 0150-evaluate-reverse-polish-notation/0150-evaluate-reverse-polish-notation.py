class Solution(object):
    def evalRPN(self, tokens):
        num_stack = []

        for t in tokens:
            if t in "+-*/":
                first = num_stack.pop()
                second = num_stack.pop()
                if t == "+":
                    num_stack.append(second + first)
                if t == "-":
                    num_stack.append(second - first)
                if t == "*":
                    num_stack.append(second * first)
                if t == "/":
                    num_stack.append(int(float(second) / first))
            else:
                num_stack.append(int(t))
        
        return num_stack[0]