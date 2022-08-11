class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## Double Binary Search O(logm * logn) O(1)
        top, bot = 0, len(matrix) - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not(top <= bot):
            return False
        
        l, r = 0, len(matrix[row]) - 1
        
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        
        return False