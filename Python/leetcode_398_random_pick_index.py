## 398. Random Pick Index
#
# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
#
# Example:
#
#     int[] nums = new int[] {1,2,3,3,3};
#     Solution solution = new Solution(nums);
#
#     // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
#     solution.pick(3);
#
#     // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
#     solution.pick(1);
##


import random
# class Solution(object):

#     arr1 = []
#     dict1 = {}

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         for key, value in enumerate(nums):
#             if value in self.dict1:
#                 self.dict1[value].append(key)
#             else:
#                 self.dict1[value] = [key]
#         self.arr1 = nums
#         print(self.arr1)
#         print(self.dict1)


#     def pick(self, target):
#         """
#         :type target: int
#         :rtype: int
#         """
#         # result = []
#         print(target)
#         return self.dict1[target][random.randint(0, len(self.dict1[target])-1)]
#         # for i in range(len(self.arr1)):
#         #     if target == self.arr1[i]:
#         #         result.append(i)
#         # print(result)
#         # return result[random.randint(0, len(result)-1)]


class Solution(object):
    arr1 = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr1 = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result = []
        for key, value in enumerate(self.arr1):
            if value == target:
                result.append(key)
        # return result[random.randint(0, len(result)-1)]
        return random.choice(result)


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 3, 3]
target = 3
obj = Solution(nums)
param_1 = obj.pick(target)
print(param_1)