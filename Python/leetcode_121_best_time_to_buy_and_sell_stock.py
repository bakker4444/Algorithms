## 121. Best Time to Buy and Sell Stock
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#     Input: [7,1,5,3,6,4]
#     Output: 5
#     Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#                 Not 7-1 = 6, as selling price needs to be larger than buying price.
#
# Example 2:
#     Input: [7,6,4,3,1]
#     Output: 0
#     Explanation: In this case, no transaction is done, i.e. max profit = 0.
##


## my solution
## dynamic programming approach
## time complexity : O(n)
## space complexity : O(n)
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        if len(prices)==2 and prices[0] > prices[1]:
            return 0

        result = [0] * (len(prices) + 1)
        result[0] = 0
        minP = prices[0]

        for i in range(len(prices)):
            result[i+1] = max(result[i], prices[i]-minP)
            if minP > prices[i]:
                minP = prices[i]
        return result[-1]


## only one or two parameter for previous max profit value
## not store all max profit value
## time complexity : O(n)
## space complexity : O(1)
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        maxP = 0
        prev = None
        for price in prices:
            if prev is not None and price > prev:
                maxP = max(maxP, price-prev)
            else:
                prev = price
        return maxP


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution1().maxProfit(prices))
    print(Solution2().maxProfit(prices))
