class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## curr: pointer which goes over the nums
        ## l: left boundry of 0 (where hasn't been sorted)
        ## r: right boundry of 2 (where hasn't been sorted)
        curr, l, r = 0, 0, len(nums) - 1
        
        def swap(i, j):
            tem = nums[i]
            nums[i] = nums[j]
            nums[j] = tem
            
        while curr <= r:
            if nums[curr] == 0:
                swap(curr, l)
                l += 1
                curr += 1
            elif nums[curr] == 2:
                swap(curr, r)
                r -= 1
            else:
                curr += 1
        
        return
    
        ## return nums.sort()
        ## Bucket Sort Solution
#         bucket_dict = {0: 0, 1: 0, 2: 0}
#         for num in nums:
#             bucket_dict[num] += 1
        
#         count_zero = bucket_dict[0]
#         count_one = bucket_dict[1]
#         count_two = bucket_dict[2]
        
#         nums[0:count_zero] = [0] * count_zero
#         nums[count_zero: count_zero + count_one] = [1] * count_one
#         nums[count_zero + count_one:] = [2] * count_two
        
#         return
        
        