class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
            return 0
        
        sign = 1
        start = 0
        
        if s[0] == "+":
            start = 1
            if len(s) == 1:
                return 0
        elif s[0] == "-":
            sign = -1
            start = 1
            if len(s) == 1:
                return 0
        
        r = ""
        for i in range(start, len(s)):
            cur = s[i]
            if cur.isdigit():
                r += cur
            else:
                break
        
        if r == "":
            return 0
        
        num = int(r) * sign
        
        if num < -2 ** 31:
            return -2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 -1
        
        return num