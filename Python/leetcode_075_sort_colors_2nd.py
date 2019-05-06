## 75. Sort Colors
#
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#     Input: [2,0,2,1,1,0]
#     Output: [0,0,1,1,2,2]
#
# Follow up:
#     - A rather straight forward solution is a two-pass algorithm using counting sort. First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
#     - Could you come up with a one-pass algorithm using only constant space?
##



### counting solution
## time complexity : O(2n)
## space complexity : O(1)
class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0]

        for val in nums:
            cnt[val] += 1
        
        for i in range(len(nums)):
            if cnt[0] != 0:
                nums[i] = 0
                cnt[0] -= 1
            elif cnt[1] != 0:
                nums[i] = 1
                cnt[1] -= 1
            else:   ## cnt[2] != 0
                nums[i] = 2
                cnt[2] -= 1
        
        return nums



### swap solution
## time complexity : O(n)
## space complexity : O(1)
class Solution2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1

        while mid <= high:
            if nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            elif nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            else:   ## nums[mid] == 1
                mid += 1

        return nums



import unittest

class Test(unittest.TestCase):
    def test_sortColors(self):
        test_input = [
            [2,0,2,1,1,0],
            [2, 0, 1],
            [1, 0, 2],
            [1, 0],
            [1, 0, 1],
            [1, 2, 1],
        ]
        test_output = [
            [0,0,1,1,2,2],
            [0, 1, 2],
            [0, 1, 2],
            [0, 1],
            [0, 1, 1],
            [1, 1, 2]
        ]
        sol1 = Solution1()
        sol2 = Solution2()

        for i in range(len(test_input)):
            result1 = sol1.sortColors(test_input[i])
            result2 = sol2.sortColors(test_input[i])
            self.assertEqual(result1, test_output[i])
            self.assertEqual(result2, test_output[i])


if __name__ == "__main__":
    unittest.main()
