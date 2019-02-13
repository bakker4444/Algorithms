## 172. Factorial Trailing Zeroes
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#     Input: 3
#     Output: 0
#     Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#     Input: 5
#     Output: 1
#     Explanation: 5! = 120, one trailing zero.
#
# Note: Your solution should be in logarithmic time complexity.
##


## iterative approach
# time complexity : O(logN)
class Solution1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n//5:
            result += n//5
            n //= 5
        return result


## recursive approach
# time complexity : O(logN)
class Solution2(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if not n else n//5 + self.trailingZeroes(n//5)



if __name__ == "__main__":
    test_input = [3, 7, 11, 315, 2436, 457457]
    test_result = [0, 1, 2, 77, 606, 114360]

    for i in range(len(test_input)):
        result1 = Solution1().trailingZeroes(test_input[i])
        result2 = Solution2().trailingZeroes(test_input[i])
        print(result1, result1 == test_result[i])
        print(result2, result2 == test_result[i])
