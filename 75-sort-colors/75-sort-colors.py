class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## return nums.sort()
        ## Bucket Sort Solution
        bucket_dict = {0: 0, 1: 0, 2: 0}
        for num in nums:
            bucket_dict[num] += 1
        
        count_zero = bucket_dict[0]
        count_one = bucket_dict[1]
        count_two = bucket_dict[2]
        
        nums[0:count_zero] = [0] * count_zero
        nums[count_zero: count_zero + count_one] = [1] * count_one
        nums[count_zero + count_one:] = [2] * count_two
        
        return nums