## 66. Plus One
#
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
#     Input: [1,2,3]
#     Output: [1,2,4]
#     Explanation: The array represents the integer 123.
#
# Example 2:
#
#     Input: [4,3,2,1]
#     Output: [4,3,2,2]
#     Explanation: The array represents the integer 4321.
##


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        carry = 0
        length1 = len(digits)
        while -length1 <= i:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                carry = 1
                digits[i] = 0
                if -length1 == i:
                    return [1] + digits
                i -= 1


if __name__ == "__main__":
    arr1 = [1, 2, 3]
    print(Solution().plusOne(arr1))
    arr1 = [4, 3, 2, 1]
    print(Solution().plusOne(arr1))
    arr1 = [0]
    print(Solution().plusOne(arr1))
