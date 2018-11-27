## 344. Reverse String
#
# Write a function that takes a string as input and returns the string reversed.
#
# Example 1:
#
#     Input: "hello"
#     Output: "olleh"
#
# Example 2:
#
#     Input: "A man, a plan, a canal: Panama"
#     Output: "amanaP :lanac a ,nalp a ,nam A"
##


## pythonic solution
class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


## traditional approach
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        i, j = 0, n-1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)


if __name__ == "__main__":
    s = "hello"
    print(Solution1().reverseString(s))
    print(Solution2().reverseString(s))

    s = "A man, a plan, a canal: Panama"
    print(Solution1().reverseString(s))
    print(Solution2().reverseString(s))