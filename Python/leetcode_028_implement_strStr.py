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


## naive solution: linear time complexity
class Solution1(object):
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


## Pattern Matching Solution: KMP matching
## Knuth–Morris–Pratt algorithm
## https://leetcode.com/problems/implement-strstr/discuss/119566/Python-KnuthMorrisPratt-algorithm
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
    def build_lps(self, pattern):
        """ Helper function for strStr.
        Returns longest proper suffix array for string pattern.
        Each lps_array[i] is the length of the longest proper prefix
        which is equal to suffix for pattern ending at character i.
        Proper means that whole string cannot be prefix or suffix.

        Time complexity: O(m). Space complexity: O(1), where
        m is the length of the pattern, space used for lps array isn't included.
        """
        m = len(pattern)
        lps_array = [0] * m
        i, j = 1, 0  # start from the 2nd character in pattern
        while i < m:
            if pattern[i] == pattern[j]:
                lps_array[i] = j + 1
                j += 1
                i += 1
            else:
                if j > 0:
                    j = lps_array[j - 1]
                else:
                    lps_array[i] = 0
                    i += 1
        return lps_array

    def strStr(self, text, pattern):
        """ Returns index of 1st occurence of pattern in text.
        Returns -1 if pattern is not in the text.
        Knuth–Morris–Pratt algorithm.
        Time complexity: O(n + m). Space complexity: O(m).
        """
        # special cases
        if not text and not pattern:
            return 0
        elif not pattern:
            return 0

        # build longest proper suffix array for pattern
        lps_array = self.build_lps(pattern)

        n, m = len(text), len(pattern)
        i, j = 0, 0
        while i < n:
            # current characters match, move to the next characters
            if text[i] == pattern[j]:
                i += 1
                j += 1
            # current characters don't match
            else:
                if j > 0:  # try start with previous longest prefix
                    j = lps_array[j - 1]
                # 1st character of pattern doesn't match character in text
                # go to the next character in text
                else:
                    i += 1

            # whole pattern matches text, match is found
            if j == m:
                return i - m

        # no match was found
        return -1




if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(Solution1().strStr(haystack, needle))
    print(Solution2().strStr(haystack, needle))

    haystack = "aaaaa"
    needle = "bba"
    print(Solution1().strStr(haystack, needle))
    print(Solution2().strStr(haystack, needle))

    haystack = "a"
    needle = "a"
    print(Solution1().strStr(haystack, needle))
    print(Solution2().strStr(haystack, needle))

    haystack = "mississippi"
    needle = "pi"
    print(Solution1().strStr(haystack, needle))
    print(Solution2().strStr(haystack, needle))
