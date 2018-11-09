## 202. Happy Number
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example:
#
#     Input: 19
#     Output: true
#     Explanation:
#         1^2 + 9^2 = 82
#         8^2 + 2^2 = 68
#         6^2 + 8^2 = 100
#         1^2 + 0^2 + 0^2 = 1
##


## another approach
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isChecked = set()
        while n != 1:
            temp = 0
            while n > 0:
                temp += pow(n%10, 2)
                n //= 10
            n = temp
            if n in isChecked:
                return False
            else:
                isChecked.add(n)
        else:
            return True


## mySolution
# class Solution(object):
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         isChecked = set()
#         while True:
#             temp = 0
#             while n >= 1:
#                 temp += pow(n%10, 2)
#                 n //= 10
#             if temp in isChecked:
#                 result = 0
#                 while temp >= 1:
#                     result += pow(temp%10, 2)
#                     temp //= 10
#                 if result == 1:
#                     return True
#                 else:
#                     return False
#             else:
#                 isChecked.add(temp)
#                 n = temp


if __name__ == "__main__":
    print(Solution().isHappy(19))
    print(Solution().isHappy(28))