class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # space O(1)
        is_col = False
        
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                is_col = True
                
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    
                    
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[0])
            
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        
        if matrix[0][0] == 0:
                matrix[0] = [0] * len(matrix[0])
        
        if is_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        return
#         space O(m + n)
#         row_zero = [1] * len(matrix)
#         col_zero = [1] * len(matrix[0])
        
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 if matrix[r][c] == 0:
#                     row_zero[r] = 0
#                     col_zero[c] = 0
        
#         for i in range(len(matrix)):
#             if row_zero[i] == 0:
#                 matrix[i] = [0] * len(matrix[0])
            
#             for j in range(len(matrix[0])):
#                 if col_zero[j] == 0:
#                     matrix[i][j] = 0
        
#         return