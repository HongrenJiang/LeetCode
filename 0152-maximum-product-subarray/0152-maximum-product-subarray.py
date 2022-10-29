class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        
        for n in nums:
            # if n == 0:
            #     currMax, currMin = 1, 1
            #     continue
            tem = currMax * n
            currMax = max(currMax * n, currMin * n, n) # could be less than old currMax, no worries, the old max has been stored in res
            currMin = min(tem, currMin * n, n)
            res = max(res, currMax, currMin)
            
        return res