class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## Brute Force Method: Time Limit Exceeded
#         maxArea = 0
#         for l in range(0, len(height)):
#             for r in range(l + 1, len(height)):
#                 width = r - l
#                 area = width * min(height[l], height[r])
#                 maxArea = max(maxArea, area)
        
#         return maxArea
        ## Two Pointer Method:
        maxArea = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            width = r - l
            area = width * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea