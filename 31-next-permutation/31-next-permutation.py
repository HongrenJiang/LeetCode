class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        pivot = 0
        
        # find the pivot
        for i in range(N - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i
                break
        
        if pivot == 0:
            nums.sort()
            return 
        
        # which is the first number > nums[pivot - 1]
        swap = N - 1
        for i in range(N - 1, pivot, -1):
            if nums[swap] > nums[pivot - 1]:
                break
            if nums[swap] <= nums[pivot - 1]:
                swap -= 1
        
        # swap
        inter = nums[swap]
        nums[swap] = nums[pivot - 1]
        nums[pivot - 1] = inter
        
        # sort after pivot
        numsPart = nums[pivot:]
        numsPart.sort()
        nums[pivot:] = numsPart
        
        