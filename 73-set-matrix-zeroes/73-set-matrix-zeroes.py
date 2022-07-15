class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero = [1] * len(matrix)
        col_zero = [1] * len(matrix[0])
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row_zero[r] = 0
                    col_zero[c] = 0
        
        for i in range(len(matrix)):
            if row_zero[i] == 0:
                matrix[i] = [0] * len(matrix[0])
            
            for j in range(len(matrix[0])):
                if col_zero[j] == 0:
                    matrix[i][j] = 0
        
        return