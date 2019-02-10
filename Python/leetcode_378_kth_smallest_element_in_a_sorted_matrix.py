## 378. Kth Smallest Element in a Sorted Matrix
#
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#     matrix = [
#         [ 1,  5,  9],
#         [10, 11, 13],
#         [12, 13, 15]
#     ],
#     k = 8,
#
#     return 13.
#
# Note:
#     You may assume k is always valid, 1 ≤ k ≤ n^2.
##


## priority queue (using heap) approach
## time complexity : O(Nlogk)
## space complexity : O(N)
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        priority_queue = []
        heapq.heapify(priority_queue)

        ## first row add to the priority queue,
        ## adding element, tuple
        ## data structure : (matrix value, row idx, col idx)
        for j in range(len(matrix[0])):
            data = (matrix[0][j], 0, j)
            heapq.heappush(priority_queue, data)

        # pop smallest number first,
        # and add the next number, which exist same column as popped number
        for i in range(k-1):
            out_tuple = heapq.heappop(priority_queue)
            if out_tuple[1] == len(matrix)-1:
                continue
            row_idx = out_tuple[1]+1
            col_idx = out_tuple[2]
            in_tuple = (matrix[row_idx][col_idx], row_idx, col_idx)
            heapq.heappush(priority_queue, in_tuple)
            del row_idx, col_idx, in_tuple
        return heapq.heappop(priority_queue)[0]



import unittest
class Test(unittest.TestCase):
    def test_kthSmallest(self):
        test_input = [
            [
                [
                    [ 1,  5,  9],
                    [10, 11, 13],
                    [12, 13, 15]
                ],
                8
            ]
        ]

        test_output = [13]

        for i in range(len(test_input)):
            result = Solution().kthSmallest(test_input[i][0], test_input[i][1])
            self.assertEqual(test_output[i], result)
            print(result)


if __name__ == "__main__":
    unittest.main()
