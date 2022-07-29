class Solution:
    def trap(self, height: List[int]) -> int:
        # Root Algo: Water = Min(MaxLeft, MaxRight) - Height[i]
        # Method 1: Extro Space : Using two list to store MaxLeft and MaxRight
        # Then use one list to sotre the minimum of the two lists.
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Method 2: Two Pointers
        # Since only care the minimum of MaxLeft and MaxRight, so we don't have
        # to know all of them. We only need to know the smaller one.
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res