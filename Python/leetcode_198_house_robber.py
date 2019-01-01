## 198. House Robber
#
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#     Input: [1,2,3,1]
#     Output: 4
#     Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#                 Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#     Input: [2,7,9,3,1]
#     Output: 12
#     Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
##                 Total amount you can rob = 2 + 9 + 1 = 12.


##  Bottom_up
##  time complexity : O(n)
##  space complexity : O(n)
class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        result = [0] * (len(nums)+1)
        result[0] = 0
        result[1] = nums[0]

        for i in range(1, len(nums)):
            result[i+1] = max(nums[i]+result[i-1], result[i])

        return result[-1]


## Top down
## time complexity: O(n)
## space complexity: O(n)
## reference
## https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.?page=4
class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.result = [0] + [nums[0]] + [-1]*(len(nums)-1)
        return self.helper(nums, len(nums))

    def helper(self, nums, idx):
        if idx == 0:
            return 0;
        if idx == 1:
            return nums[0];
        if self.result[idx] >= 0:
            return self.result[idx]
        self.result[idx] = max( nums[idx-1]+ self.helper(nums, idx-2) , self.helper(nums, idx-1) )
        return self.result[idx]



## bottom up optimization
## time complexity : O(n)
## space complexity : O(1)
## reference
## https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.?page=4
class Solution3(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        prev1 = 0
        prev2 = 0
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp
        return prev1




if __name__ == "__main__":
    print(Solution1().rob([1,2,3,1]))
    print(Solution2().rob([1,2,3,1]))
    print(Solution3().rob([1,2,3,1]))

    print(Solution1().rob([2,7,9,3,1]))
    print(Solution2().rob([2,7,9,3,1]))
    print(Solution3().rob([2,7,9,3,1]))

    print(Solution1().rob([19,3,48,23,43,22,28]))
    print(Solution2().rob([19,3,48,23,43,22,28]))
    print(Solution3().rob([19,3,48,23,43,22,28]))