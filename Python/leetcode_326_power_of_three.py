## 326. Power of Three
#
# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#     Input: 27
#     Output: true
#
# Example 2:
#     Input: 0
#     Output: false
#
# Example 3:
#     Input: 9
#     Output: true
#
# Example 4:
#     Input: 45
#     Output: false
#
# Follow up:
#     Could you do it without using any loop / recursion?
##


## reference
## https://leetcode.com/problems/power-of-three/solution/
## Approach #1 Loop Iteration
class Solution1(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


## reference
## https://leetcode.com/problems/power-of-three/solution/
## Approach #4 Integer Limitations
class Solution2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19 % n == 0


if __name__ == "__main__":
    for i in range(20):
        print("i =", i, "\t", "n =", 3**i, ":", Solution1().isPowerOfThree(3**i))
    print()
    for i in range(20):
        print("i =", i, "\t", "n =", 3**i, ":", Solution2().isPowerOfThree(3**i))
