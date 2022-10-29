class Solution:
    def simple_rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            tem = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tem
        
        return rob2
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        reward1 = self.simple_rob(nums[1:])
        reward2 = self.simple_rob(nums[:-1])
        
        return max(reward1, reward2)