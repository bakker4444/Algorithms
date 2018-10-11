## 461. Hamming Distance
#
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
#     0 ≤ x, y < 2^31.
#
# Example:
#
#     Input: x = 1, y = 4
#
#     Output: 2
#
#     Explanation:
#     1   (0 0 0 1)
#     4   (0 1 0 0)
#            ↑   ↑
#
#     The above arrows point to positions where the corresponding bits are different.
##


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # if x < 0 or x >= 2**31 or y < 0 or y >= 2**31:
        #     return -1

        hamming_number = x ^ y
        result = 0
        while hamming_number:
            if hamming_number & 1:
                result += 1
            hamming_number >>= 1
        return result


if __name__ == "__main__":
    print(Solution().hammingDistance(1, 4))
    print(Solution().hammingDistance(42, 82))
    print(Solution().hammingDistance(12345, 98765))
