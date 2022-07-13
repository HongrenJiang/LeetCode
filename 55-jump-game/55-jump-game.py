class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        l = r = 0
        farest = 0
        
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farest = max(farest, i + nums[i])
            if farest == r:
                break
            l = r + 1
            r = farest
        
        if r >= last:
            return True
        else:
            return False