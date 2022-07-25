class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 2: One-Pass Hash Table (Find the diff from the past)
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hashMap = { } # val -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [i, hashMap[diff]]
            hashMap[num] = i
        
        # # Method 1: Brute Force
        # # Time Complexity: O(C(n,2)) = O(n(n-1)/2) = O(n^2)
        # # Space Complexity: O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]