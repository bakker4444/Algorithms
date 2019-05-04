## 678. Valid Parenthesis String
#
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
#     1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#     2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
#     3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#     4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
#     5. An empty string is also valid.
#
# Example 1:
#     Input: "()"
#     Output: True
#
# Example 2:
#     Input: "(*)"
#     Output: True
#
# Example 3:
#     Input: "(*))"
#     Output: True
#
# Note:
#     The string size will be in the range [1, 100].
##


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low, high = 0, 0
        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                low -= 1
                high -= 1
            else:   ## c == "*"
                low -= 1
                high += 1
            
            if high < 0:
                return False

            low = max(low, 0)

        return low == 0



import unittest

class Test(unittest.TestCase):
    def test_checkValidString(self):
        test_input = [ "()", "(*)", "(*))" ]
        test_output = [ True, True, True ]
        sol = Solution()
        for i in range(len(test_input)):
            result = sol.checkValidString(test_input[i])
            self.assertEqual(result, test_output[i])


if __name__ == "__main__":
    unittest.main()        