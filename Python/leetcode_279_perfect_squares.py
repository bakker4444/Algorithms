## 279. Perfect Squares
#
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#     Input: n = 12
#     Output: 3
#     Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#     Input: n = 13
#     Output: 2
#     Explanation: 13 = 4 + 9.
##


## BFS search
## reference : https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n

        i = 0
        perfect_square_list = []

        while i**2 <= n:
            perfect_square_list.append(i**2)
            i += 1

        count_result = 0
        check_numbers = {n}

        while check_numbers:
            count_result += 1
            temp_set = set()
            for num in check_numbers:
                for perfect_num in perfect_square_list:
                    if num == perfect_num:
                        return count_result
                    if num < perfect_num:
                        break
                    temp_set.add(num-perfect_num)
            check_numbers = temp_set

        return count_result


if __name__ == "__main__":
    print(Solution().numSquares(12))
    print(Solution().numSquares(13))
    print(Solution().numSquares(43))
    print(Solution().numSquares(4))

