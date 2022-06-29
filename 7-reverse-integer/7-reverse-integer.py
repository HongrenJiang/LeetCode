class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            s = str(x)
            s = s[::-1]
            r = int(s)
        
        if x < 0:
            s = str(-x)
            s = s[::-1]
            r = int(s) * (-1)
        
        if r <= -2**31 or r > 2**31 -1:
            return 0
        
        return r