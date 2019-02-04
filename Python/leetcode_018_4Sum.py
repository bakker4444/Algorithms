## 18. 4Sum
#
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#     The solution set must not contain duplicate quadruplets.
#
# Example:
#     Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
#     A solution set is:
#         [
#             [-1,  0, 0, 1],
#             [-2, -1, 1, 2],
#             [-2,  0, 0, 2]
#         ]
##


## reference : https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
## recursive approach down to two sum problem
## time complexity : not sure, O(N^3) or O(N^2*logN)
## space complexity : not sure also
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNSum(nums, target, 4, [], results)
        return results

    def findNSum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return

        ## solve 2Sum
        if N == 2:
            lIdx, rIdx = 0, len(nums)-1

            while lIdx < rIdx:
                if nums[lIdx] + nums[rIdx] == target:
                    results.append(result + [nums[lIdx], nums[rIdx]])
                    lIdx += 1
                    rIdx -= 1

                    ## duplicate move lIdx and rIdx
                    while lIdx < rIdx and nums[lIdx] == nums[lIdx-1]:
                        lIdx += 1
                    while lIdx < rIdx and nums[rIdx] == nums[rIdx+1]:
                        rIdx -= 1

                elif nums[lIdx] + nums[rIdx] < target:
                    lIdx += 1
                else:   ## nums[lIdx] + nums[rIdx] > target
                    rIdx -= 1

        ## higher order or N-Sum
        else:
            for i in range(0, len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findNSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return


import unittest
class Test(unittest.TestCase):
    def test_fourSum(self):
        test_input = [
            [
                [1, 0, -1, 0, -2, 2], 0
            ]
        ]
        test_result = [
            [
                [-2, -1, 1, 2],
                [-2,  0, 0, 2],
                [-1,  0, 0, 1],
            ]
        ]
        for i in range(len(test_input)):
            result = Solution().fourSum(test_input[i][0], test_input[i][1])
            self.assertEqual(result, test_result[i])
            print(result)


if __name__ == "__main__":
    unittest.main()