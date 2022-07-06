class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # openN == closeN == n, append new answer
        # openN < n, add new open
        # closeN < openN, add new close
        stack = []
        res = []
        
        def backTrace(n, openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backTrace(n, openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backTrace(n, openN, closeN + 1)
                stack.pop()
        
        backTrace(n, 0, 0)
        return res