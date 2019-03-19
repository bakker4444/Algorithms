## 191. Number of 1 Bits
#
# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
#
# Example 1:
#     Input: 00000000000000000000000000001011
#     Output: 3
#     Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
#
# Example 2:
#     Input: 00000000000000000000000010000000
#     Output: 1
#     Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
#
# Example 3:
#     Input: 11111111111111111111111111111101
#     Output: 31
#     Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
#
# Note:
#     * Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
#     * In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
#
# Follow up:
#     * If this function is called many times, how would you optimize it?
##


## Time complexity : O(1), 32 times comparison
## Space complexity : O(1)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n >> 1
        return count



import unittest

class Test(unittest.TestCase):
    def test_hammingWeight(self):
        test_input = [
            0b00000000000000000000000000001011,
            0b00000000000000000000000010000000,
            0b11111111111111111111111111111101
        ]
        test_output = [ 3, 1, 31 ]

        for i in range(len(test_input)):
            result = Solution().hammingWeight(test_input[i])
            self.assertEqual(result, test_output[i])
            print(result)



if __name__ == "__main__":
    unittest.main()