## 189. Rotate Array
#
# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
#     Input: [1,2,3,4,5,6,7] and k = 3
#     Output: [5,6,7,1,2,3,4]
#     Explanation:
#         rotate 1 steps to the right: [7,1,2,3,4,5,6]
#         rotate 2 steps to the right: [6,7,1,2,3,4,5]
#         rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
#
#     Input: [-1,-100,3,99] and k = 2
#     Output: [3,99,-1,-100]
#     Explanation:
#         rotate 1 steps to the right: [99,-1,-100,3]
#         rotate 2 steps to the right: [3,99,-1,-100]
#
# Note:
#
#     Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#     Could you do it in-place with O(1) extra space?
##


## approach 1: concaternate and slice
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[length-k:] + nums[:length-k]
        print(nums)

        # ## shorter expression
        # nums[:] = (nums[len(nums)-k%len(nums):] + nums[:len(nums)-k%len(nums)])
        # print(nums)


if __name__ == "__main__":
    arr1, k = [1, 2, 3, 4, 5, 6, 7], 3
    Solution().rotate(arr1, k)
    arr1, k = [-1, -100, 3, 99], 2
    Solution().rotate(arr1, k)