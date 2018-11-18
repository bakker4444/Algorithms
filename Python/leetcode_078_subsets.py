## 78. Subsets
#
# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#     Input: nums = [1,2,3]
#     Output:
#     [
#         [3],
#         [1],
#         [2],
#         [1,2,3],
#         [1,3],
#         [2,3],
#         [1,2],
#         []
#     ]
##


## approach 1
## reference : https://leetcode.com/problems/subsets/discuss/122645/3ms-easiest-solution-no-backtracking-no-bit-manipulation-no-dfs-no-bullshit
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            result += [ x + [num] for x in result ]
        return result


if __name__ == "__main__":
    arr1 = [1, 2, 3]
    print(Solution().subsets(arr1))

    arr1 = [3, 4, 1, 2]
    print(Solution().subsets(arr1))
