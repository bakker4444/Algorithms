## 1. Two Sum
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
#     Given nums = [2, 7, 11, 15], target = 9,
#
#     Because nums[0] + nums[1] = 2 + 7 = 9,
#     return [0, 1].
##


## approach 2: unsorted array
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numSeen = {}
        for i in range(len(nums)):
            if nums[i] in numSeen:
                return [numSeen[nums[i]], i]
            else:
                numSeen[target - nums[i]] = i


## approach 1: initial idea, sorted array
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         loidx = 0
#         hiidx = len(nums)-1
#         while loidx < hiidx:
#             sum1 = nums[loidx] + nums[hiidx]
#             if sum1 == target:
#                 return [loidx, hiidx]
#             elif sum1 < target:
#                 loidx += 1
#             else:
#                 hiidx -= 1
#         return False


if __name__ == "__main__":
    arr1 = [2, 7, 11, 15]
    target1 = 9
    print(Solution().twoSum(arr1, target1))
    arr1 = [3, 2, 4]
    target1 = 6
    print(Solution().twoSum(arr1, target1))