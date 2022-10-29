class Solution:
    def simple_rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        reward = [nums[0], nums[1]]
        temMax = 0
        
        for i in range(2, len(nums)):
            temMax = max(temMax, reward[i - 2])
            reward.append(temMax + nums[i])
        
        # print(reward)
        return max(reward[-1], reward[-2])
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        reward1 = self.simple_rob(nums[1:])
        reward2 = self.simple_rob(nums[:-1])
        
        return max(reward1, reward2)