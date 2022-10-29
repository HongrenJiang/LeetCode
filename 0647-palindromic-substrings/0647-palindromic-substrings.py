class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        for i in range(0, len(s)):
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res