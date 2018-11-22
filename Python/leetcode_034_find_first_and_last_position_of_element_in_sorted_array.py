## 34. Find First and Last Position of Element in Sorted Array
#
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#     Input: nums = [5,7,7,8,8,10], target = 8
#     Output: [3,4]
#
# Example 2:
#
#     Input: nums = [5,7,7,8,8,10], target = 6
#     Output: [-1,-1]
##


## binary search
## https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not len(nums):
            return [-1, -1]

        result = [0] * 2
        i, j = 0, len(nums)-1

        while i < j:
            mid = (i+j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                j = mid

        if nums[i] == target:
            result[0] = i
        else:
            result[0] = -1

        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j) // 2 + 1
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid

        if nums[j] == target:
            result[1] = j
        else:
            result[1] = -1

        return result


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(Solution().searchRange(nums, target))

    nums = []
    target = 0
    print(Solution().searchRange(nums, target))
