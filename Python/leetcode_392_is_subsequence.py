## 392. Is Subsequence
#
# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
#     s = "abc", t = "ahbgdc"
#
#     Return true.
#
# Example 2:
#     s = "axc", t = "ahbgdc"
#
#     Return false.
#
# Follow up:
#     If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
##


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ## another approach
        current_idx = -1
        for character in s:
            current_idx = t.find(character, current_idx+1)
            if current_idx == -1:
                return False
        return True


        ## my approach
        # s_idx = 0
        # t_idx = 0
        # while s_idx < len(s) and t_idx < len(t):
        #     if s_idx == len(s):
        #         return True
        #     if s[s_idx] != t[t_idx]:
        #         t_idx += 1
        #     else:
        #         s_idx += 1
        #         t_idx += 1
        # if s_idx == len(s):
        #     return True
        # else:
        #     return False


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))
    s = "axc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))