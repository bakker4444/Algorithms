## 33. Search in Rotated Sorted Array
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#     Input: nums = [4,5,6,7,0,1,2], target = 0
#     Output: 4
#
# Example 2:
#
#     Input: nums = [4,5,6,7,0,1,2], target = 3
#     Output: -1
##


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        loIdx, hiIdx = 0, len(nums)-1
        while loIdx < hiIdx:
            midIdx = (hiIdx + loIdx) // 2
            if nums[midIdx] > nums[hiIdx]:
                loIdx = midIdx + 1
            else:
                hiIdx = midIdx
        # print(loIdx, midIdx, hiIdx)

        junc = loIdx

        loIdx, hiIdx = 0, len(nums)-1
        while loIdx <= hiIdx:
            midIdx = (hiIdx + loIdx) // 2
            oriIdx = (midIdx + junc) % len(nums)
            if nums[oriIdx] == target:
                return oriIdx
            if nums[oriIdx] < target:
                loIdx = midIdx + 1
            else:
                hiIdx = midIdx - 1
        return -1


if __name__ == "__main__":
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 4
    print(Solution().search(arr1, target1))
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 5
    print(Solution().search(arr1, target1))
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 6
    print(Solution().search(arr1, target1))
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 7
    print(Solution().search(arr1, target1))
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print(Solution().search(arr1, target1))
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 1
    print(Solution().search(arr1, target1))
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 2
    print(Solution().search(arr1, target1))
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 3
    print(Solution().search(arr1, target1))
