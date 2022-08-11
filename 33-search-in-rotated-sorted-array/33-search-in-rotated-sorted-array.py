class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # [4, 5, 6, 7, 8, 9, 0, 1, 2] left portion
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else: 
                    r = mid - 1
            else:
                # [5, 6, 7, 0, 1, 2, 3, 4] right portion
                # if nums[l] > nums[mid]:
                # This part you can't use 'if nums[l] > nums[mid]:'
                # because l will be updated, but you want to use the old l
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1