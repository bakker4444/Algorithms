## 507. Perfect Number
#
# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
#
# Example:
#     Input: 28
#     Output: True
#     Explanation: 28 = 1 + 2 + 4 + 7 + 14
#
# Note: The input number n will not exceed 100,000,000. (1e8)
##


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        result = 1
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                result += divisor
                if num / divisor != divisor:
                    result += num // divisor
            divisor += 1
        return True if result == num else False


if __name__ == "__main__":
    print(str(5) + " : " + str(Solution().checkPerfectNumber(5)))
    print(str(6) + " : " + str(Solution().checkPerfectNumber(6)))
    print(str(28) + " : " + str(Solution().checkPerfectNumber(28)))
    print(str(8128) + " : " + str(Solution().checkPerfectNumber(8128)))
    print(str(33550336) + " : " + str(Solution().checkPerfectNumber(33550336)))