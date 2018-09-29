## 122. Best Time to Buy and Sell Stock II
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
#     Input: [7,1,5,3,6,4]
#     Output: 7
#     Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#                  Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#
# Example 2:
#
#     Input: [1,2,3,4,5]
#     Output: 4
#     Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#                 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#                 engaging multiple transactions at the same time. You must sell before buying again.
#
# Example 3:
#
#     Input: [7,6,4,3,1]
#     Output: 0
#     Explanation: In this case, no transaction is done, i.e. max profit = 0.
##


## approach 2: only tracking differences
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0

        maxReturn = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                maxReturn += prices[i] - prices[i-1]
        return maxReturn


## approach 1: finding peak and valley
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         # set profit index
#         # set maxReturn
#         # using runner compare profit index element and runner's one
#         # if profit index element < runner's element, then add the difference to the maxReturn
#         if not prices or len(prices) == 1:
#             return 0

#         profitIndex = 0
#         maxReturn = 0
#         for i in range(1, len(prices)):
#             if prices[i-1] <= prices[i]:
#                 continue
#             elif prices[i-1] > prices[i]:
#                 maxReturn += prices[i-1] - prices[profitIndex]
#                 profitIndex = i
#         if prices[profitIndex] < prices[i]:
#             maxReturn += prices[i] - prices[profitIndex]
#         return maxReturn


if __name__ == "__main__":
    arr1 = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(arr1))
    arr1 = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(arr1))
    arr1 = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(arr1))
    arr1 = [6, 1, 3, 2, 4, 7]
    print(Solution().maxProfit(arr1))