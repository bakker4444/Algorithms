## 240. Search a 2D Matrix II
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
# Example:
#     Consider the following matrix:
#     [
#         [1,   4,  7, 11, 15],
#         [2,   5,  8, 12, 19],
#         [3,   6,  9, 16, 22],
#         [10, 13, 14, 17, 24],
#         [18, 21, 23, 26, 30]
#     ]
#
#     Given target = 5, return true.
#     Given target = 20, return false.
##


## start with right top corner
## time complexity : O(m+n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while col >= 0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            if matrix[row][col] < target:
                row += 1

        return False

if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    targets = [5, 20, 7, 8, 29, 33]

    for target in targets:
        print("Target",target, ":", Solution().searchMatrix(matrix, target))
