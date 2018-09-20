## 9. Palindrome Number
#
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Follow up:
# Coud you solve it without converting the integer to a string?
#

##################################################################

## Approach 2: Number --> reverse half of the digits and compare those two
## consider with memory overflow
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ## check negative number
        if x < 0:
            return False

        ## check the last digit is 0 --> always false
        if (x % 10 == 0) and (x != 0):
            return False

        ## revert half of digits
        revertedNumber = 0
        while (x > revertedNumber):
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        ## compare and return
        return (x == revertedNumber) or (x == revertedNumber // 10)


## test
if __name__ == "__main__":
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(123))


##################################################################

# ## Approach 1: String
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#
#         ## check x is negative --> return false
#         if x < 0:
#             return False
#
#         if 0 <= x <= 9:
#             return True
#
#         # string conversion
#         x = str(x)
#
#         ## set front and last runner
#         front = 0
#         last = len(str(x))
#         for front in range(len(x)//2):
#             if x[front] is not x[last-1-front]:
#                 return False
#         return True
#
#
# if __name__ == "__main__":
#     print(Solution().isPalindrome(121))
#     print(Solution().isPalindrome(-121))
#     print(Solution().isPalindrome(123))

