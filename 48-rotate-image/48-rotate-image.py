class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix[0]) - 1
        
        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                # positions of four cornors
                topleft = matrix[top][l + i]
                # topright = matrix[top + i][r]
                # bottomleft = matrix[bottom - i][l]
                # bottomright = matrix[bottom][r - i]
                
                # rotate
                tem = topleft
                matrix[top][l + i] = matrix[bottom - i][l] # change topleft
                matrix[bottom - i][l] = matrix[bottom][r - i] # change bottomleft
                matrix[bottom][r - i] = matrix[top + i][r] # change bottomright
                matrix[top + i][r] = tem # change topright
            
            l += 1
            r -= 1
        
        return