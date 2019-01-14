## 84. Largest Rectangle in Histogram
#
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#           6
#         5 *
#         * *
#         * *   3
#     2   * * 2 *
#     * 1 * * * *
#     * * * * * *
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# Example:
#
#     Input: [2,1,5,6,2,3]
#     Output: 10
##


## reference : https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
## time complexity : O(n)
## using stack data structure
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans


if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(Solution().largestRectangleArea(heights))