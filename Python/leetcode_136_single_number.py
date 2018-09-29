## 136. Single Number
#
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
#     Input: [2,2,1]
#     Output: 1
#
# Example 2:
#
#     Input: [4,1,2,1,2]
#     Output: 4
##


## approach 2: using XOR characteristic, remove duplicate
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result


# ## approach 1: using dict, with boolean
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dict1 = {}
#         for num in nums:
#             if num in dict1:
#                 del dict1[num]
#             else:
#                 dict1[num] = True
#         for key in dict1:
#             return key


import unittest

class TestSolution(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(Solution().singleNumber([2, 2, 1]), 1)
        self.assertEqual(Solution().singleNumber([4,1,2,1,2]), 4)
        self.assertEqual(Solution().singleNumber([1]), 1)


if __name__ == "__main__":
    unittest.main()