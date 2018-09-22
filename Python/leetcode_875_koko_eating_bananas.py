## 875. Koko Eating Bananas
#
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.
# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
# Return the minimum integer K such that she can eat all the bananas within H hours.
#
# Example 1:
#     Input: piles = [3,6,7,11], H = 8
#     Output: 4
#
# Example 2:
#     Input: piles = [30,11,23,4,20], H = 5
#     Output: 30
#
# Example 3:
#     Input: piles = [30,11,23,4,20], H = 6
#     Output: 23
#
#
# Note:
#     1 <= piles.length <= 10^4
#     piles.length <= H <= 10^9
#     1 <= piles[i] <= 10^9
##


class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        minPile = 1
        maxPile = max(piles)

        while (minPile <= maxPile):
            hourNeeded = 0
            middlePileNum = minPile + (maxPile - minPile) // 2
            # print("middlePileNum : " + str(middlePileNum))
            for pile in piles:
                if pile <= middlePileNum:
                    hourNeeded += 1
                elif pile % middlePileNum != 0:
                    hourNeeded += pile // middlePileNum + 1;
                else:
                    hourNeeded += pile // middlePileNum

            if hourNeeded <= H:
                maxPile = middlePileNum - 1
            else:
                minPile = middlePileNum + 1

        return minPile



if __name__ == "__main__":
    input = [3,6,7,11]
    H = 8
    print(Solution().minEatingSpeed(input, H))  ## 4

    input = [30,11,23,4,20]
    H = 5
    print(Solution().minEatingSpeed(input, H))  ## 30

    input = [30,11,23,4,20]
    H = 6
    print(Solution().minEatingSpeed(input, H))  ## 23
