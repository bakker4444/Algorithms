## 53. Maximum Subarray
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
#     Input: [-2,1,-3,4,-1,2,1,-5,4],
#     Output: 6
#     Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Follow up:
#
#     If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
##


## reference
## https://leetcode.com/problems/maximum-subarray/discuss/20194/A-Python-solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return False

        currentSum = nums[0]
        maximumSum = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], nums[i]+currentSum)
            maximumSum = max(currentSum, maximumSum)

        return maximumSum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))