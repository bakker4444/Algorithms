## 166 Fraction to Recurring Decimal
#
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# Example 1:
#     Input: numerator = 1, denominator = 2
#     Output: "0.5"
#
# Example 2:
#     Input: numerator = 2, denominator = 1
#     Output: "2"
#
# Example 3:
#     Input: numerator = 2, denominator = 3
#     Output: "0.(6)"
##



## reference : https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51114/Python-solution
## python 3
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""

        # check the result sign
        if numerator / denominator < 0:
            result += "-"

        if numerator % denominator == 0:
            return str(numerator//denominator)

        numerator, denominator = abs(numerator), abs(denominator)

        result += str(numerator//denominator)
        result += "."

        numerator %= denominator

        idx = len(result)
        memo = dict()

        while numerator != 0:
            if numerator not in memo:
                memo[numerator] = idx
            else:
                idx = memo[numerator]
                result = result[:idx] + "(" + result[idx:] + ")"
                return result
            numerator *= 10
            result += str(numerator//denominator)
            numerator %= denominator
            idx += 1
        return result



if __name__ == "__main__":
    test_input = [ [1, 2], [2, 1], [2, 3] ]
    test_output = [ "0.5", "2", "0.(3)" ]

    for i in range(len(test_input)):
        result = Solution().fractionToDecimal(test_input[i][0], test_input[i][1])
        print(result)


