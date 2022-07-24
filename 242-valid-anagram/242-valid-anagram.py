class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method 2: Frequency Counting
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # 0 is the default value
            countT[t[i]] = 1 + countT.get(t[i], 0) # it's for the first time
        
        for c in countS:
            if countS[c] != countT.get(c, 0): # countT[c] may cause error
                return False
        
        return True
#         # Method 1: Sorting
#         # Time Complexity: O(nlog(n))
#         # Space Complexity: O(1)
#         _s = sorted(s)
#         _t = sorted(t)
        
#         if _s == _t:
#             return True
#         else:
#             return False