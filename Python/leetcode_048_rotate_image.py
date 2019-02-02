## You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#     You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
#     Given input matrix =
#         [
#             [1,2,3],
#             [4,5,6],
#             [7,8,9]
#         ],
#
#     rotate the input matrix in-place such that it becomes:
#         [
#             [7,4,1],
#             [8,5,2],
#             [9,6,3]
#         ]
#
# Example 2:
#     Given input matrix =
#         [
#             [ 5, 1, 9,11],
#             [ 2, 4, 8,10],
#             [13, 3, 6, 7],
#             [15,14,12,16]
#         ],
#
#     rotate the input matrix in-place such that it becomes:
#         [
#             [15,13, 2, 5],
#             [14, 3, 4, 1],
#             [12, 6, 8, 9],
#             [16, 7,10,11]
#         ]
##


## rotate ring by ring
## time complexity : O(N^2)
## space complexity : O(1)
## reference : https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
class Solution1(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        sIdx = 0
        eIdx = n-1
        while sIdx < eIdx:
            for i in range(eIdx-sIdx):
                matrix[sIdx][sIdx+i], matrix[sIdx+i][eIdx] = matrix[sIdx+i][eIdx], matrix[sIdx][sIdx+i]
                matrix[sIdx][sIdx+i], matrix[eIdx][eIdx-i] = matrix[eIdx][eIdx-i], matrix[sIdx][sIdx+i]
                matrix[sIdx][sIdx+i], matrix[eIdx-i][sIdx] = matrix[eIdx-i][sIdx], matrix[sIdx][sIdx+i]
            sIdx += 1
            eIdx -= 1

        return matrix


## rotate clockwise : two way to change
#       method 1)   transpose    ->      reverse horizontally
#               1 2 3           1 4 7           7 4 1
#               4 5 6    -->    2 5 8    -->    8 5 2
#               7 8 9           3 6 9           9 6 3
#
#       method 2)   reverse vertically  ->   transpose
#               1 2 3           7 8 9           7 4 1
#               4 5 6    -->    4 5 6    -->    8 5 2
#               7 8 9           1 2 3           9 6 3
#
## rotate counterclockwise :
#       method 1)   transpose    -->    reverse vertically
#               1 2 3           1 4 7           3 6 9
#               4 5 6    -->    2 5 8    -->    2 5 8
#               7 8 9           3 6 9           1 4 7
#
#       method 2)   reverse horizontally  ->   transpose
#               1 2 3           3 2 1           3 6 9
#               4 5 6    -->    6 5 4    -->    2 5 8
#               7 8 9           9 8 7           1 4 7
#
## transpose and reverse horizontally
## time complexity : O(N^2)
## space complexity : O(1)
class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        ## transpose
        for i in range(n):
            for j in range(i, n):
                self.swap(matrix[i][j], matrix[j][i])

        ## reverse horizontally
        for i in range(n):
            for j in range(n//2):
                self.swap(matrix[i][j], matrix[i][n-1-j])

        return matrix

    def swap(self, num1, num2):
        temp = num1
        num1 = num2
        num2 = temp




import unittest

class Test(unittest.TestCase):
    def test_rotate(self):
        test_cases = [
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ],
            [
                [ 5, 1, 9,11],
                [ 2, 4, 8,10],
                [13, 3, 6, 7],
                [15,14,12,16]
            ]
        ]

        test_results = [
            [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ],
            [
                [15,13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7,10,11]
            ]
        ]

        for i in range(len(test_cases)):
            result1 = Solution1().rotate(test_cases[i])
            result2 = Solution2().rotate(test_cases[i])
            self.assertEqual(result1, test_results[i])
            self.assertEqual(result2, test_results[i])
            print(result1)
            print(result2)



if __name__ == "__main__":
    unittest.main()
