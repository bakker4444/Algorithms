## 171. Excel Sheet Column Number
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
#
# Example 1:
#
#     Input: "A"
#     Output: 1
#
# Example 2:
#
#     Input: "AB"
#     Output: 28
#
# Example 3:
#
#     Input: "ZY"
#     Output: 701
##


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        power = 0
        while s:
            lastStr = s[len(s)-1]
            result += (ord(lastStr)-64) * (26**power)
            power += 1
            s = s[:-1]
        return result


if __name__ == "__main__":
    str1 = "A"
    print(Solution().titleToNumber(str1))
    str1 = "AB"
    print(Solution().titleToNumber(str1))
    str1 = "ZY"
    print(Solution().titleToNumber(str1))

