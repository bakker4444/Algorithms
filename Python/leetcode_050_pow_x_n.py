## 50. Pow(x, n)
#
# Implement pow(x, n), which calculates x raised to the power n (xn).
# http://www.cplusplus.com/reference/valarray/pow/
#
# Example 1:
#
#     Input: 2.00000, 10
#     Output: 1024.00000
#
# Example 2:
#
#     Input: 2.10000, 3
#     Output: 9.26100
#
# Example 3:
#
#     Input: 2.00000, -2
#     Output: 0.25000
#     Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
# Note:
#
#     -100.0 < x < 100.0
#     n is a 32-bit signed integer, within the range [−231, 231 − 1]
##


## recursion with helper function
class Solution1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # obvious solution
        # return x**n

        if x == 0:
            return 0
        if n == 0:
            return 1
        if n > 0:
            return self.calc(x, n)
        return 1/self.calc(x, -n)

    def calc(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent % 2 == 0:
            return self.calc(base*base, exponent//2)
        else:
            return base * self.calc(base*base, exponent//2)


## another approach without helper function
class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 1:
            x = 1/x
            n = -n
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)


## amazing solution : exponent bit manipulation
## https://leetcode.com/problems/powx-n/discuss/19563/Iterative-Log(N)-solution-with-Clear-Explanation


if __name__ == "__main__":
    x, n = 2.00000, 10
    print(Solution1().myPow(x, n))
    print(Solution2().myPow(x, n))

    x, n = 0.00001, 2147483647
    print(Solution1().myPow(x, n))
    print(Solution2().myPow(x, n))

    x, n = 2.10000, 3
    print(Solution1().myPow(x, n))
    print(Solution2().myPow(x, n))

    x, n = 2.00000, -2147483648
    print(Solution1().myPow(x, n))
    print(Solution2().myPow(x, n))
