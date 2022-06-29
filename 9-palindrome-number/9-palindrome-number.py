class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        
        if len(s) % 2:
            #odd length
            l, r = len(s) // 2, len(s) // 2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            if l == -1:
                return True
            else:
                return False
        else:
            #even length
            l, r = int(len(s) / 2 - 1), int(len(s) / 2)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            if l == -1:
                return True
            else:
                return False