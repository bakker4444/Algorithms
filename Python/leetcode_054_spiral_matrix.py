## 54. Spiral Matrix
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#     Input:
#         [
#             [ 1, 2, 3 ],
#             [ 4, 5, 6 ],
#             [ 7, 8, 9 ]
#         ]
#     Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
#     Input:
#         [
#             [1, 2, 3, 4],
#             [5, 6, 7, 8],
#             [9,10,11,12]
#         ]
#     Output: [1,2,3,4,8,12,11,10,9,5,6,7]
##


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        result = []
        iStart, iEnd = 0, len(matrix) - 1
        jStart, jEnd =0, len(matrix[0]) - 1

        while iStart <= iEnd and jStart <= jEnd:
            ## right
            for j in range(jStart, jEnd+1):
                result.append(matrix[iStart][j])
            iStart += 1

            ## down
            for i in range(iStart, iEnd+1):
                result.append(matrix[i][jEnd])
            jEnd -= 1

            ## left
            if iStart <= iEnd:
                for j in range(jEnd, jStart-1, -1):
                    result.append(matrix[iEnd][j])
                iEnd -= 1

            ## up
            if jStart <= jEnd:
                for i in range(iEnd, iStart-1, -1):
                    result.append(matrix[i][jStart])
                jStart += 1

            # print(iStart, iEnd, jStart, jEnd)
        return result


if __name__ == "__main__":
    arr = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    result = Solution().spiralOrder(arr)
    assert result == [1,2,3,6,9,8,7,4,5]
    print(result)

    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    result = Solution().spiralOrder(arr)
    assert result == [1,2,3,4,8,12,11,10,9,5,6,7]
    print(result)
