## 769. Max Chunks To Make Sorted
#
# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
#
# What is the most number of chunks we could have made?
#
# Example 1:
#     Input: arr = [4,3,2,1,0]
#     Output: 1
#     Explanation:
#         Splitting into two or more chunks will not return the required result.
#         For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
#
# Example 2:
#     Input: arr = [1,0,2,3,4]
#     Output: 4
#     Explanation:
#         We can split into two chunks, such as [1, 0], [2, 3, 4].
#         However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
#
# Note:
#     - arr will have length in range [1, 10].
#     - arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
##



## time complexity : O(n), n == len(arr)
## space complexity : O(1)
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        currentMax = -1
        result = 0

        for i, v in enumerate(arr):
            currentMax = max(currentMax, v)
            if currentMax == i:
                result += 1
        
        return result



import unittest

class Test(unittest.TestCase):
    def test_maxChunksToSorted(self):
        test_input = [
            [4,3,2,1,0],
            [1,0,2,3,4]
        ]
        test_output = [1, 4]
        sol = Solution()

        for i in range(len(test_input)):
            result = sol.maxChunksToSorted(test_input[i])
            self.assertEqual(result, test_output[i])



if __name__ == "__main__":
    unittest.main()