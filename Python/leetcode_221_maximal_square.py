## 221. Maximal Square
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#     Input:
#         1 0 1 0 0
#         1 0 1 1 1
#         1 1 1 1 1
#         1 0 0 1 0
#     Output: 4
##



## approach : Dynamic programming
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        memo = [ [ 0 for _ in range(len(matrix[0])+1) ] for _ in range(len(matrix)+1) ]

        for i in range(len(matrix[0])):
            memo[1][i+1] = int(matrix[0][i])

        max_len = 0

        for row in range(1, len(matrix)+1):
            for col in range(1, len(matrix[0])+1):
                if matrix[row-1][col-1] == "0":
                    memo[row][col] = 0
                else:
                    memo[row][col] = 1 + min(memo[row-1][col], memo[row-1][col-1], memo[row][col-1])
                if max_len < memo[row][col]:
                    max_len = memo[row][col]

        return max_len ** 2


import unittest
class Test(unittest.TestCase):
    def test_maximalSquare(self):
        test_input = [
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]
            ],
            [
                ["1", "1", "1", "0", "0", "1"],
                ["1", "1", "1", "1", "1", "1"],
                ["1", "1", "1", "1", "1", "1"],
                ["1", "0", "1", "1", "1", "1"],
                ["1", "0", "1", "1", "1", "1"]
            ]
        ]
        test_output = [4, 16]

        from pprint import pprint

        for i in range(len(test_input)):
            pprint(test_input[i])
            result = Solution().maximalSquare(test_input[i])
            self.assertEqual(result, test_output[i])
            pprint(result)



if __name__ == "__main__":
    unittest.main()
