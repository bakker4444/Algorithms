## 322. Coin Change
#
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#     Input: coins = [1, 2, 5], amount = 11
#     Output: 3
#     Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#     Input: coins = [2], amount = 3
#     Output: -1
#
# Note:
#     You may assume that you have an infinite number of each kind of coin.
##


## dynamic programming: bottom-up
## reference
## https://leetcode.com/problems/coin-change/discuss/77360/C++-O(n*amount)-time-O(amount)-space-DP-solution
class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        maximum = amount + 1
        numOfCoins = [maximum] * (amount+1)
        numOfCoins[0] = 0

        for total in range(maximum):
            for j in range(len(coins)):
                if coins[j] <= total:
                    numOfCoins[total] = min(numOfCoins[total], numOfCoins[total-coins[j]]+1)

        return -1 if numOfCoins[amount] > amount else numOfCoins[amount]



## similar like backpack problem
##     - capacity of the "backpack" is amount
##     - coins represents value of each item you can put into the "backpack"
##     - you can take 0 or many coins
##     - for each coin the cost is constant 1
##     - so the question is to find minimum cost to fill the "backpack"
##
## reference
## https://leetcode.com/problems/coin-change/discuss/141031/Python-5-line-solution-It's-actually-a-complete-backpack-problem
class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[-1] if dp[-1] != float('inf') else -1



if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    result1 = Solution1().coinChange(coins, amount)
    result2 = Solution2().coinChange(coins, amount)
    print(result1, result2)

    coins = [2]
    amount = 3
    result1 = Solution1().coinChange(coins, amount)
    result2 = Solution2().coinChange(coins, amount)
    print(result1, result2)

    coins = [2, 3, 7, 11]
    amount = 3877
    result1 = Solution1().coinChange(coins, amount)
    result2 = Solution2().coinChange(coins, amount)
    print(result1, result2)
