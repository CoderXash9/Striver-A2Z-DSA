class Solution:
    def searchMatrix(self, mat, target):
        rows, cols = len(mat), len(mat[0])

        top, bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > mat[row][-1]:
                top = row + 1
            elif target < mat[row][0]:
                bot = row - 1
            else:
                break

        if top > bot:
            return False

        row = (top + bot) // 2
        l, r = 0, cols - 1

        while l <= r:
            m = (l + r) // 2

            if target > mat[row][m]:
                l = m + 1
            elif target < mat[row][m]:
                r = m - 1
            else:
                return True

        return False