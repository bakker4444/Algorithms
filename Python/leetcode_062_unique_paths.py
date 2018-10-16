## 62. Unique Paths
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#     Input: m = 3, n = 2
#     Output: 3
#     Explanation:
#     From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#     1. Right -> Right -> Down
#     2. Right -> Down -> Right
#     3. Down -> Right -> Right
#
# Example 2:
#
#     Input: m = 7, n = 3
#     Output: 28
##


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 0 or n < 0:
            return 0
        if m == 1 or n == 1:
            return 1

        arr1 = [ [0 for i in range(m)] for j in range(n)]
        arr1[0][0] = 1

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    pass
                if i-1 >= 0:
                    arr1[i][j] += arr1[i-1][j]
                if j-1 >= 0:
                    arr1[i][j] += arr1[i][j-1]

        return arr1[n-1][m-1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 2))
    print(Solution().uniquePaths(7, 3))
