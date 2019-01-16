## 44. Wildcard Matching
#
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#     '?' Matches any single character.
#     '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# Note:
#     s could be empty and contains only lowercase letters a-z.
#     p could be empty and contains only lowercase letters a-z, and characters like ? or *.
#
# Example 1:
#     Input:
#         s = "aa"
#         p = "a"
#     Output: false
#     Explanation: "a" does not match the entire string "aa".
#
# Example 2:
#     Input:
#         s = "aa"
#         p = "*"
#     Output: true
#     Explanation: '*' matches any sequence.
#
# Example 3:
#     Input:
#         s = "cb"
#         p = "?a"
#     Output: false
#     Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#
# Example 4:
#     Input:
#         s = "adceb"
#         p = "*a*b"
#     Output: true
#     Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
#
# Example 5:
#     Input:
#         s = "acdcb"
#         p = "a*c?b"
#     Output: false
##


## reference 1 : http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
## reference 2 : https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution
## Time Complexity : O(n)
## Space Complexity : O(1)
class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sIdx = 0
        pIdx = 0
        sMatchLocation = 0
        pStarLocation = -1

        while sIdx < len(s):
            if pIdx < len(p) and (s[sIdx] == p[pIdx] or p[pIdx]=="?" ):
                sIdx += 1
                pIdx += 1
            elif pIdx < len(p) and p[pIdx] == "*":
                sMatchLocation = sIdx
                pStarLocation = pIdx
                pIdx += 1
            elif (pStarLocation != -1):
                pIdx = pStarLocation + 1
                sMatchLocation += 1
                sIdx = sMatchLocation
            else:
                return False
        while pIdx < len(p) and p[pIdx] == "*":
            pIdx += 1

        return pIdx == len(p)



## Solution 2 : Dynamic programming bottom up method
## time complexity : O(m*n)
## space complexity : O(m*n)
## reference : https://www.youtube.com/watch?v=3ZDZ-N0EPV0



if __name__ == "__main__":
    inputStrings = [
        ["aa", "a"],            ## False
        ["aa", "*"],            ## True
        ["cb", "?a"],           ## False
        ["adceb", "*a*b"],      ## True
        ["acdcb", "a*c?b"],     ## False
    ]
    for s, p in inputStrings:
        print(Solution().isMatch(s, p))