## 387. First Unique Character in a String
#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
#     s = "leetcode"
#     return 0
#
#     s = "loveleetcode",
#     return 2
#
# Note: You may assume the string contain only lowercase letters.
##


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        check = dict()
        for c in s:
            if c in check:
                check[c] = False
            else:
                check[c] = True

        for i in range(len(s)):
            if check[s[i]]:
                return i
        return -1


if __name__ == "__main__":
    s = "leetcode"
    print(Solution().firstUniqChar(s))

    s = "loveleetcode"
    print(Solution().firstUniqChar(s))