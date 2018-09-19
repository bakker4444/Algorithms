# # 7. Reverse Integer
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
# Input: 123
# Output: 321
#
# Example 2:
# Input: -123
# Output: -321
#
# Example 3:
# Input: 120
# Output: 21
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        ## sign info saved
        isNegative = True if x < 0 else False
        x = abs(x)

        reversedNumber = 0

        while x >= 1:
            reversedNumber += int(x % 10)

            ## overflow check if x if positive
            if not isNegative and reversedNumber > (pow(2,31) - 1):
                return 0

            ## overflow check if x is negative
            elif isNegative and reversedNumber > pow(2,31):
                return 0

            ## last digit should not multiply by 10
            if x >= 10:
                reversedNumber *= 10

            ## integer division
            x //= 10

        return int(reversedNumber) if (not isNegative) else (-1 * int(reversedNumber))


## test
if __name__ == "__main__":
    print(pow(2,31)-1)
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(2147447412))
    print(Solution().reverse(-2147483648))



