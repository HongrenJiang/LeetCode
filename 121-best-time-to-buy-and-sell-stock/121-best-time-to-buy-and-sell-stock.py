class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Method 2: Sliding Window
        # Updating the minimum left
        # O(n) O(1)
        res = 0
        l = 0
        
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r           
            res = max(res, prices[r] - prices[l])
        
        return res
    
#         # Method 1: Brute Force Time: O(n!)=O(n^2) Space: O(1)
#         # For the problem, Brute Force is very similar with Sliding Window
#         res = 0
#         l = 0
        
#         for l in range(len(prices)):
#             r = l + 1
#             for r in range(l, len(prices)):
#                 if prices[r] > prices[l]:
#                     res = max(res, prices[r] - prices[l])
        
#         return res