## 152. Maximum Product Subarray
#
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
#     Input: [2,3,-2,4]
#     Output: 6
#     Explanation: [2,3] has the largest product 6.
#
# Example 2:
#
#     Input: [-2,0,-1]
#     Output: 0
#     Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
##


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = current_max
                current_max = current_min
                current_min = temp
                del temp

            current_max = max(nums[i], current_max*nums[i])
            current_min = min(nums[i], current_min*nums[i])

            result = max(result, current_max)

        return result


if __name__ == "__main__":
    arr1 = [2, 3, -2, 4]
    print(Solution().maxProduct(arr1))
    arr1 = [-2, 0, -1]
    print(Solution().maxProduct(arr1))
