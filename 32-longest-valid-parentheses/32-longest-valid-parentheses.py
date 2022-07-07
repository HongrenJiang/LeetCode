class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # the index before 'the first'(maybe) left parentheses
        mx = 0
        
        for i, c in enumerate(s):
            # print()
            # print("index: " + str(i))
            # print("stack at beginning: " + str(stack))
            # print("mx: " + str(mx))
            if c == "(":
                stack.append(i)
            elif c == ")":
                stack.pop()
                # finish a
                if not stack:
                    # new start
                    # maybe the index before 'the new first' left parentheses
                    # because of pop, will be updated automatically
                    stack.append(i)
                else:
                    # the newest right parentheses' index 
                    # minus ( the counterpart's index minus 1)
                    mx = max(mx, i - stack[-1])
            # print("stack at last: " + str(stack))
        
        return mx