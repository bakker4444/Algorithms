## 200. Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#     Input:
#     11110
#     11010
#     11000
#     00000
#
#     Output: 1
#
# Example 2:
#     Input:
#     11000
#     11000
#     00100
#     00011
#
#     Output: 3
##



## BFS with visited node
## time complexity : O(N^2)
## space complexity : [NOT SURE] O(1) or O(N^2) for recursive call stacks
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    cnt += 1
                    self.helper(row, col, grid, cnt)
        return cnt

    def helper(self, row, col, grid, cnt):
        if (row < 0) or (row > len(grid) - 1) or (col < 0) or (col > len(grid[0]) - 1):
            return

        if grid[row][col] == "1":
            grid[row][col] = "0"
            self.helper(row-1, col, grid, cnt)
            self.helper(row+1, col, grid, cnt)
            self.helper(row, col-1, grid, cnt)
            self.helper(row, col+1, grid, cnt)



import unittest

class Test(unittest.TestCase):
    def test_numIslands(self):
        test_input = [
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
        ]
        test_result = [1, 3]

        for i in range(len(test_input)):
            result = Solution().numIslands(test_input[i])
            self.assertEqual(test_result[i], result)
            print(result)


if __name__ == "__main__":
    unittest.main()