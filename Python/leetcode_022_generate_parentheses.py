## 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = n
        right = n
        result = []
        element = ""
        self.backtrack(result, element, left, right, n)
        return result

    def backtrack(self, result, element, left, right, n):
        if right < left:
            return

        if not left and not right:
            result.append(element)
            return

        if left:
            self.backtrack(result, element+"(", left-1, right, n)

        if right:
            self.backtrack(result, element+")", left, right-1, n)


## test
if __name__ == "__main__":
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(2))
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))
