## 128. Longest Consecutive Sequence
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#     Input: [100, 4, 200, 1, 3, 2]
#     Output: 4
#     Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
##


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set(nums)
        longest_length = 0
        for element in set1:
            if element-1 not in set1:
                next_element = element + 1
                while next_element in set1:
                    next_element += 1
                longest_length = max(longest_length, next_element-element)
        return longest_length


if __name__ == "__main__":
    set1 = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(set1))
