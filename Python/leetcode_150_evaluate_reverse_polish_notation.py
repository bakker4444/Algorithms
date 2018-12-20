## 150. Evaluate Reverse Polish Notation
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation(https://en.wikipedia.org/wiki/Reverse_Polish_notation).
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Note:
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
#
# Example 1:
#     Input: ["2", "1", "+", "3", "*"]
#     Output: 9
#     Explanation: ((2 + 1) * 3) = 9
#
# Example 2:
#     Input: ["4", "13", "5", "/", "+"]
#     Output: 6
#     Explanation: (4 + (13 / 5)) = 6
#
# Example 3:
#     Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#     Output: 22
#     Explanation:
#           ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#         = ((10 * (6 / (12 * -11))) + 17) + 5
#         = ((10 * (6 / -132)) + 17) + 5
#         = ((10 * 0) + 17) + 5
#         = (0 + 17) + 5
#         = 17 + 5
#         = 22
##


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        calc = {"+","-","*","/"}
        result = []
        for element in tokens:
            if element in calc:
                right = result.pop()
                left = result.pop()
                result.append(int(self.helper(left, right, element)))
            else:
                result.append(int(element))
        return result.pop()

    def helper(self, left, right, operation):
        if operation in {"+","-","*"}:
            left = int(left)
        else:
            left = float(left)
        right = int(right)

        if operation == "+":
            return left+right
        elif operation == "-":
            return left-right
        elif operation == "*":
            return left*right
        else:   ## operation == "/"
            return left/right


if __name__ == "__main__":
    testCase = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        ["8"]
    ]
    for case in testCase:
        print(Solution().evalRPN(case))
