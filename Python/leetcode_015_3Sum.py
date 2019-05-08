## 15. 3Sum
#
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#     The solution set must not contain duplicate triplets.
#
# Example:
#     Given array nums = [-1, 0, 1, 2, -1, -4],
#     A solution set is:
#         [
#             [-1, 0, 1],
#             [-1, -1, 2]
#         ]
##


### using two-sum method,  a+b+c = 0 <==> a+b = -c
## time complexity : O(N*N)
## space complexity : O(N)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N = len(nums)
        result = []

        for i in range(N):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -1 * nums[i]
            left, right = i+1, N-1

            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            
        return result




import unittest

class Test(unittest.TestCase):
    def test_threeSum(self):
        test_input = [
            [-1, 0, 1, 2, -1, -4]
        ]
        test_output = [
            [
                [-1, -1, 2],
                [-1, 0, 1]
            ]
        ]

        sol = Solution()

        for i in range(len(test_input)):
            result = sol.threeSum(test_input[i])
            self.assertEqual(result, test_output[i])


if __name__ == "__main__":
    unittest.main()
