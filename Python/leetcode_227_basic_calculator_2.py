## 227. Basic Calculator II
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# Example 1:
#     Input: "3+2*2"
#     Output: 7
#
# Example 2:
#     Input: " 3/2 "
#     Output: 1
#
# Example 3:
#     Input: " 3+5 / 2 "
#     Output: 5
#
# Note:
#     You may assume that the given expression is always valid.
#     Do not use the eval built-in library function.
##



## time complexity : O(N)
## space complexity : O(N)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        stacks = []
        sign = "+"      ## initial setup

        for i in range(len(s)):
            ## number makes
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            ## operation : +, -, *, /
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stacks.append(-num)
                elif sign == "+":
                    stacks.append(num)
                elif sign == "*":
                    stacks.append(stacks.pop()*num)
                else:
                    temp_val = stacks.pop()
                    if temp_val / num < 0 and temp_val % num != 0:
                        stacks.append(temp_val//num + 1)
                    else:
                        stacks.append(temp_val//num)
                num = 0
                sign = s[i]

        ## sum all stacks number
        return sum(stacks)



import unittest
class Test(unittest.TestCase):
    def test_calculate(self):
        test_input = [
            "3+2*2",
            " 3/2 ",
            " 3+5 / 2 ",
            "14-3/2"
        ]
        test_output = [7, 1, 5, 13]

        for i in range(len(test_input)):
            result = Solution().calculate(test_input[i])
            self.assertEqual(test_output[i], result)
            print(result)



if __name__ == "__main__":
    unittest.main()