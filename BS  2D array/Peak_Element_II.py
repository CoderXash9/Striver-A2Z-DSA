class Solution:
    def findPeakGrid(self, mat):

        rows = len(mat)
        cols = len(mat[0])

        left = 0
        right = cols - 1

        while left <= right:

            mid = (left + right) // 2

            # Find row having maximum element in mid column
            max_row = 0

            for r in range(rows):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r

            # Left neighbour
            if mid - 1 >= 0:
                left_value = mat[max_row][mid - 1]
            else:
                left_value = -1

            # Right neighbour
            if mid + 1 < cols:
                right_value = mat[max_row][mid + 1]
            else:
                right_value = -1

            # Peak found
            if mat[max_row][mid] > left_value and mat[max_row][mid] > right_value:
                return [max_row, mid]

            # Move left
            elif left_value > mat[max_row][mid]:
                right = mid - 1

            # Move right
            else:
                left = mid + 1