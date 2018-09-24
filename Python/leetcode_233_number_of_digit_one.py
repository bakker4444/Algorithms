## 233. Number of Digit One
#
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
#
# Example:
#
# Input: 13
# Output: 6
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        result = 0
        m = 1
        while m <= n:
            divider = m * 10
            result += (n // divider) * m + min(max(n % divider - m + 1, 0), m)
            m *= 10
        return result



if __name__ == "__main__":
    print(Solution().countDigitOne(1))
    print(Solution().countDigitOne(10))
    print(Solution().countDigitOne(13))
    print(Solution().countDigitOne(3184191))
