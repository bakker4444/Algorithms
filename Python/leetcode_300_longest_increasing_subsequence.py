## 300. Longest Increasing Subsequence
#
# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
#     Input: [10,9,2,5,3,7,101,18]
#     Output: 4
#     Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
#     There may be more than one LIS combination, it is only necessary for you to return the length.
#     Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
##


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = [0] * len(nums)
        size = 0

        for num in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if LIS[m] < num:
                    i = m + 1
                else:
                    j = m
            LIS[i] = num
            size = max(i+1, size)
        return size


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))
