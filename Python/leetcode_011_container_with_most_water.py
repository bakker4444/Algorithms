## 11. Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#            8       *                   *
#            7       *-------------------*-------*
#            6       *   *               *       *
#            5       *   *       *       *       *
#            4       *   *       *   *   *       *
#            3       *   *       *   *   *   *   *
#            2       *   *   *   *   *   *   *   *
#            1   *   *   *   *   *   *   *   *   *
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#
# Example:
#
#    Input: [1,8,6,2,5,4,8,3,7]
#    Output: 49
##


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_idx = 0
        right_idx = len(height) - 1
        max_water = 0
        while left_idx < right_idx:
            max_water = max(max_water, (right_idx-left_idx) * min(height[left_idx], height[right_idx]))
            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
        return max_water


if __name__ == "__main__":
    arr1 = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(arr1))