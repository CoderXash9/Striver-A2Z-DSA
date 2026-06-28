from bisect import bisect_right


class Solution:
    def findMedian(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Minimum and maximum values in the matrix
        low = min(row[0] for row in matrix)
        high = max(row[-1] for row in matrix)

        required = (rows * cols) // 2

        while low <= high:

            mid = (low + high) // 2

            count = 0

            # Count elements <= mid
            for row in matrix:
                count += bisect_right(row, mid)

            if count <= required:
                low = mid + 1
            else:
                high = mid - 1

        return low
