## 69. Sqrt(x)
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#     Input: 4
#     Output: 2
#
# Example 2:
#     Input: 8
#     Output: 2
#     Explanation: The square root of 8 is 2.82842..., and since
#                 the decimal part is truncated, 2 is returned.
##


## Binary search
## time complexity : O(logN)
## space complexity : O(1)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        left = 0
        right = x//2

        while (left<=right):
            mid = left + (right-left)//2

            if mid*mid == x:
                return mid

            elif mid*mid > x:
                right = mid - 1

            elif mid*mid <= x:
                if (mid+1)*(mid+1) > x:
                    return mid
                left = mid + 1


if __name__ == "__main__":
    for i in range(0, 100, 10):
        print("int(sqrt("+str(i)+")) :", Solution().mySqrt(i))