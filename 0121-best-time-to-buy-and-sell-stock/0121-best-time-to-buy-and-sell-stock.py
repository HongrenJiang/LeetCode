class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 0
        
        while l <= r:
            if r == len(prices) - 1:
                break
            r = r + 1
            pro = prices[r] - prices[l]
            res = max(res, pro)
            if (prices[r] < prices[l]):
                l = r
        
        return res