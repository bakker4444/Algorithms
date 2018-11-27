## 28. Implement strStr()
#
# Implement strStr().
# http://www.cplusplus.com/reference/cstring/strstr/
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
#     Input: haystack = "hello", needle = "ll"
#     Output: 2
#
# Example 2:
#
#     Input: haystack = "aaaaa", needle = "bba"
#     Output: -1
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
# http://www.cplusplus.com/reference/cstring/strstr/
# https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)
##


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        len_n = len(needle)

        for i in range(len(haystack)-len_n+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len_n] == needle:
                    return i
        return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(Solution().strStr(haystack, needle))

    haystack = "aaaaa"
    needle = "bba"
    print(Solution().strStr(haystack, needle))

    haystack = "a"
    needle = "a"
    print(Solution().strStr(haystack, needle))

    haystack = "mississippi"
    needle = "pi"
    print(Solution().strStr(haystack, needle))
