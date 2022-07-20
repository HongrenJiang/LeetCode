class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        
        def dfs(i):
            # out of bound, because maybe it will jump 2 letters at once
            # so we need to think about i == len(s)
            if i in dp:
                return dp[i]
            
            # s[i] == '0', dead end
            # dead end judge shoud be before the normal end/edge of bound judge
            if s[i] == '0':
                return 0
            
            
            res = dfs(i + 1)
            
            if int(s[i: i + 2]) <= 26 and i + 1 < len(s):
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)