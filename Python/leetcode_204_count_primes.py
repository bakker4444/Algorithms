## 204. Count Primes
#
# Count the number of prime numbers LESS THAN a non-negative number, n.
#
# Example:
#
#     Input: 10
#     Output: 4
#     Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
##


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        count = 0

        board = [ True ] * n
        board[0], board[1] = False, False

        for i in range(2, int(n**0.5)+1):
            if board[i]:
                for j in range(i*i, n, i):
                    board[j] = False
        for k in board:
            if k:
                count += 1
        return count


if __name__ == "__main__":
    arr = [2, 4, 10, 32, 100, 543, 1000, 10000]
    for num in arr:
        print("Count Prime less than", num, ":",Solution().countPrimes(num))
