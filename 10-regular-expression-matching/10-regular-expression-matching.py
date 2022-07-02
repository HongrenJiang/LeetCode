class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Recursion + Memoization
        # The difficult part of the promblem is "*", because if it's ".", it matches.
        # But if it's "*", there is two possibility: "" (0 of preceding element)
        # and repeat any times
        # The good way is to use pointers, i is for s and j is for p
        # If we choose "0", i = i and j = j + 2, j jumps the "*"
        # If we choose "repeat 1 more time", i = i + 1 and j = j
        
        def recM(i, j):
            # Think about when to stop
            if i >= len(s) and j >= len(p):
                return True
            elif i < len(s) and j >= len(p):
                return False
            else:
                # if i >= len(s) and j < len(p):
                # Not sure, because "*" can make the preceding disappear
                # if i < len(s) and j < len(p)
                # We havn't finished the matching
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                # if the next p letter is "*"
                if (j + 1) < len(p) and (p[j + 1] == "*"):
                    return (recM(i, j + 1 + 1) 
                            or (match and recM(i + 1, j)))
                # if the next p letter is not "*"
                if match:
                    # check the next letter pair
                    return recM(i + 1, j + 1)
                
                return False
            
        return recM(0, 0)
        # The above method hasn't used the memoization, so it's slow
        # I will do this in the followings