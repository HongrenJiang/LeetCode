class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        res = 1
        tem = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                tem += 1
                res = max(res, tem)
            elif nums[i] - nums[i - 1] != 0:
                tem = 1
        
        return res