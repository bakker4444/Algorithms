## 334. Increasing Triplet Subsequence
#
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
#
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
#
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Example 1:
#     Input: [1,2,3,4,5]
#     Output: true
#
# Example 2:
#     Input: [5,4,3,2,1]
#     Output: false
##


## reference : https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
## time complexity : O(n)
## space complexity : O(1)
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False



if __name__ == "__main__":
    print(Solution().increasingTriplet([1,2,3,4,5]))
    print(Solution().increasingTriplet([]))
    print(Solution().increasingTriplet([0,1,2]))
    print(Solution().increasingTriplet([0]))
    print(Solution().increasingTriplet([1,0]))
    print(Solution().increasingTriplet([2,1,0]))
    print(Solution().increasingTriplet([5,4,3,2,1]))
    print(Solution().increasingTriplet([5,2,1,7,4]))
    print(Solution().increasingTriplet([4,3,1,9,2,7]))
    print(Solution().increasingTriplet([2,1,5,0,3]))
    print(Solution().increasingTriplet([5,2,1,4,7]))