## 75. Sort Colors
#
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
#     Input: [2,0,2,1,1,0]
#     Output: [0,0,1,1,2,2]
#
# Follow up:
#
#     - A rather straight forward solution is a two-pass algorithm using counting sort. First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
#     - Could you come up with a one-pass algorithm using only constant space?
##


## approach : two flag, front-side and end-side
## point : while condition, white_idx <= blue_idx
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 0: red, 1: white, 2: blue
        red_idx = 0
        white_idx = 0
        blue_idx = len(nums) - 1

        while white_idx <= blue_idx:
            if nums[white_idx] == 0:    # 0: red, front
                self.changeTwoElements(nums, red_idx, white_idx)
                white_idx += 1
                red_idx += 1
            elif nums[white_idx] == 2:     ## 2: blue, end
                self.changeTwoElements(nums, white_idx, blue_idx)
                blue_idx -= 1
            else:   #if nums[white_idx] == 1:    # 1: white, middle
                white_idx += 1

    def changeTwoElements(self, nums, x, y):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)

    nums = [2, 0, 1]
    Solution().sortColors(nums)
    print(nums)

    nums = [1, 0, 2]
    Solution().sortColors(nums)
    print(nums)

    nums = [1, 0]
    Solution().sortColors(nums)
    print(nums)

    nums = [1, 0, 1]
    Solution().sortColors(nums)
    print(nums)

    nums = [1, 2, 1]
    Solution().sortColors(nums)
    print(nums)
