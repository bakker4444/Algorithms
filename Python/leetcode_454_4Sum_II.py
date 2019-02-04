## 454. 4Sum II
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.
#
# Example:
#
#     Input:
#         A = [ 1, 2]
#         B = [-2,-1]
#         C = [-1, 2]
#         D = [ 0, 2]
#
#     Output:
#         2
#
#     Explanation:
#         The two tuples are:
#             1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
#             2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
##


## two N^2 nested for loop with dictionary approach
## time complexity : O(N^2)
## space complexity : O(N^2)
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        temp = dict()
        for a in A:
            for b in B:
                if a+b in temp:
                    temp[a+b] += 1
                else:
                    temp[a+b] = 1
        result = 0
        for c in C:
            for d in D:
                if -c-d in temp:
                    result += temp[-c-d]
        return result



import unittest
class Test(unittest.TestCase):
    def test_fourSumCount(self):
        test_input = [
            [
                [ 1, 2],
                [-2,-1],
                [-1, 2],
                [ 0, 2]
            ]
        ]
        test_output = [2]

        for i in range(len(test_input)):
            result = Solution().fourSumCount(test_input[i][0], test_input[i][1], test_input[i][2], test_input[i][3])
            print(result)
            self.assertEqual(result, test_output[i])



if __name__ == "__main__":
    unittest.main()