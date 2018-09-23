# 442. Find All Duplicates in an Array
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
#     Input:
#     [4,3,2,7,8,2,3,1]

#     Output:
#     [2,3]
##


## check duplication using array's index
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            index = abs(num)-1
            if nums[index] < 0:
                result.append(index+1)
            else:
                nums[index] *= -1
        return result


if __name__ == "__main__":
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDuplicates(nums1))
