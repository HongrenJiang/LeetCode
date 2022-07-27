class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Method 2: Prefix and Postfix Product
        # Time Complexity: O(n)
        # Space Complexity: O(n) if we use two array to store the prefix and postfix
        # Space Complexity: O(1) if we manipulate the res directly
        res = [1] * len(nums)
        prefix = 1
        
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        
        
#         # Brute Force is easy but the complexity is high
#         # Total Product divided by num doesn't work because of 0
#         # Time Complexity: O(n^2) Time Limit Exceeded
#         # Space Complexity: O(1)
#         res = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if j != i:
#                     res[i] = res[i] * nums[j]
        
#         return res