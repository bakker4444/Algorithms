## 324. Wiggle Sort II
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example 1:
#
#     Input: nums = [1, 5, 1, 1, 6, 4]
#     Output: One possible answer is [1, 4, 1, 5, 1, 6].
#
# Example 2:
#
#     Input: nums = [1, 3, 2, 2, 3, 1]
#     Output: One possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
#     You may assume all input has valid answer.
#
# Follow Up:
#     Can you do it in O(n) time and/or in-place with O(1) extra space?
##


## very hard
## need to understand quick select concept, median of medians concept
## reference
## https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
class Solution1(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        print(nums)
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        print(nums)


class Solution2(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2]) - 1
        print(nums)
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
        print(nums)




if __name__ == "__main__":
    nums = [1, 5, 1, 1, 6, 4]
    print(Solution1().wiggleSort(nums))
    nums = [1, 5, 1, 1, 6, 4]
    print(Solution2().wiggleSort(nums))

    nums = [1, 3, 2, 2, 3, 1]
    print(Solution1().wiggleSort(nums))
    nums = [1, 3, 2, 2, 3, 1]
    print(Solution2().wiggleSort(nums))

