class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _s = sorted(s)
        _t = sorted(t)
        
        if _s == _t:
            return True
        else:
            return False