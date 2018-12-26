## 46. Permutations
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#     Input: [1,2,3]
#     Output:
#         [
#             [1,2,3],
#             [1,3,2],
#             [2,1,3],
#             [2,3,1],
#             [3,1,2],
#             [3,2,1]
#         ]
##


## my approach, dfs

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]

        result = []

        self.dfs(nums, [], result)
        return  result

    def dfs(self, nums, path, result):
        if len(nums) == 0:
            result.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)


if __name__ == "__main__":
    print(Solution().permute([1]))
    print(Solution().permute([1,2]))
    print(Solution().permute([1,2,3]))
    print(Solution().permute([1,2,3,4]))