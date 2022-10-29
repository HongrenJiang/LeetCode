class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[amount/sum] = number of coins
        dp = [math.inf] * (amount + 1) # 0, 1, ... amout
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        
        return dp[-1] if dp[-1] != math.inf else -1