class Solution:
    def searchMatrix(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        rows = 0
        cols = m - 1
        while rows < n and cols >= 0:
            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] < target:
                rows += 1
            else:
                cols = cols - 1
        return False
    
