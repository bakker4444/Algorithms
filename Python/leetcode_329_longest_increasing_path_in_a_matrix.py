## 329. Longest Increasing Path in a Matrix
#
# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#     Input: nums =
#         [
#             [9,9,4],
#             [6,6,8],
#             [2,1,1]
#         ]
#     Output: 4
#     Explanation: The longest increasing path is [1, 2, 6, 9].
#
# Example 2:
#     Input: nums =
#         [
#             [3,4,5],
#             [3,2,6],
#             [2,2,1]
#         ]
#     Output: 4
#     Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
##


## approach : DFS with memoization
## reference : https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms?page=1
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not len(matrix) or not len(matrix[0]):
            return 0

        def dfs(row, col):
            if not memo[row][col]:
                value = matrix[row][col]
                memo[row][col] = 1 + max(
                    dfs(row-1, col) if row and value > matrix[row-1][col] else 0,
                    dfs(row+1, col) if row < len(matrix)-1 and value > matrix[row+1][col] else 0,
                    dfs(row, col-1) if col and value > matrix[row][col-1] else 0,
                    dfs(row, col+1) if col < len(matrix[0])-1 and value > matrix[row][col+1] else 0
                )
            return memo[row][col]

        memo = [[ 0 for _ in range(len(matrix[0]))] for _ in range(len(matrix)) ]
        return max(dfs(row, col) for row in range(len(matrix)) for col in range(len(matrix[0])))



import unittest

class Test(unittest.TestCase):
    def test_longestIncreasingPath(self):
        test_input = [
            [
                [9,9,4],
                [6,6,8],
                [2,1,1]
            ],
            [
                [1,2]
            ]
        ]
        test_result = [4, 2]

        for i in range(len(test_input)):
            result = Solution().longestIncreasingPath(test_input[i])
            self.assertEqual(result, test_result[i])
            print(result)


if __name__ == "__main__":
    unittest.main()