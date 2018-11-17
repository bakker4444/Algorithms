## 162. Find Peak Element
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
#     Input: nums = [1,2,3,1]
#     Output: 2
#     Explanation: 3 is a peak element and your function should return the index number 2.
#
# Example 2:
#
#     Input: nums = [1,2,1,3,5,6,4]
#     Output: 1 or 5
#     Explanation: Your function can return either index number 1 where the peak element is 2,
#                 or index number 5 where the peak element is 6.
#
# Note:
#
# Your solution should be in logarithmic complexity.
##


## case 1: linear search
class Solution1(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1


## case 2: Recursive Binary Search
class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = (len(nums) - 1) // 2
        ## one element
        if len(nums) == 1:
            return 0
        ## decending
        if nums[mid] > nums[mid+1]:
            return 1 + self.findPeakElement(nums[:mid])
        ## ascending
        else:
            return mid + self.findPeakElement(nums[mid:])


## case 3: Iterative Binary Search
class Solution3(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx < right_idx:
            mid = (left_idx + right_idx) // 2
            if nums[mid] > nums[mid+1]:
                right_idx = mid
            else:
                left_idx = mid + 1
        return left_idx


if __name__ == "__main__":
    arr1 = [1, 2, 3, 1]
    answer1 = Solution1().findPeakElement(arr1)
    answer2 = Solution2().findPeakElement(arr1)
    answer3 = Solution3().findPeakElement(arr1)
    print(answer1, 2 == answer1)
    print(answer2, 2 == answer2)
    print(answer3, 2 == answer3)

    arr1 = [1, 2, 1, 3, 5, 6, 4]
    answer1 = Solution1().findPeakElement(arr1)
    answer2 = Solution2().findPeakElement(arr1)
    answer3 = Solution3().findPeakElement(arr1)
    print(answer1, 1 == answer1 or 5 == answer1)
    print(answer2, 1 == answer2 or 5 == answer2)
    print(answer3, 1 == answer3 or 5 == answer3)

