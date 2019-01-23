## 20. Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#     1. Open brackets must be closed by the same type of brackets.
#     2. Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
# Example 1:
#     Input: "()"
#     Output: true
#
# Example 2:
#     Input: "()[]{}"
#     Output: true
#
# Example 3:
#     Input: "(]"
#     Output: false
#
# Example 4:
#     Input: "([)]"
#     Output: false
#
# Example 5:
#     Input: "{[]}"
#     Output: true
##


## time complexity : O(N)
## space complexity : O(N)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 0:
            return True

        mark = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                mark.append(s[i])

            else:
                if (not len(mark)) \
                    or (s[i] == ")" and mark[-1] != "(") \
                    or (s[i] == "}" and mark[-1] != "{") \
                    or (s[i] == "]" and mark[-1] != "["):
                    return False
                else:
                    mark.pop()

        return mark == []



if __name__ == "__main__":
    inArr = [
        "()[]{}", "(]", "([)]", "{[]}", "",
        ")", "]", "}", "(", "[",
        "{"
    ]
    check = [
        True, False, False, True, True,
        False, False, False, False, False,
        False
    ]
    result = Solution()
    for i in range(len(inArr)):
        assert check[i] == result.isValid(inArr[i])
        print(result.isValid(inArr[i]))
