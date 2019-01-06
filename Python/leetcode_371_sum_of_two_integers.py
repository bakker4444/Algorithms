## 371. Sum of Two Integers
#
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example 1:
#     Input: a = 1, b = 2
#     Output: 3
#
# Example 2:
#     Input: a = -2, b = 3
#     Output: 1
##


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF

        # 32 bits interger min
        MIN = 0x80000000

        # mask to get last 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


if __name__ == "__main__":
    a, b = 1, 2
    print(Solution().getSum(a, b))
    a, b = -1, 1
    print(Solution().getSum(a, b))
    a, b = -1, 0
    print(Solution().getSum(a, b))
