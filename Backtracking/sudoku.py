class Solution:
    
    def is_valid(self, mat, row, col, num):
        # Check if 'num' can be placed in the row
        for i in range(9):
            if mat[row][i] == num:
                return False
        
        # Check if 'num' can be placed in the column
        for i in range(9):
            if mat[i][col] == num:
                return False
        
        # Check if 'num' can be placed in the 3x3 sub-grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if mat[i][j] == num:
                    return False
        
        return True

    def solveSudoku(self, mat):
        # Find an empty cell (denoted by 0)
        for row in range(9):
            for col in range(9):
                if mat[row][col] == 0:
                    # Try each number from 1 to 9
                    for num in range(1, 10):
                        if self.is_valid(mat, row, col, num):
                            mat[row][col] = num
                            
                            # Recursively attempt to solve the rest of the grid
                            if self.solveSudoku(mat):
                                return True
                            
                            # Backtrack if placing num didn't lead to a solution
                            mat[row][col] = 0
                    
                    # If no number from 1 to 9 works, return False
                    return False
        
        # If the grid is fully filled, return True
        return True

