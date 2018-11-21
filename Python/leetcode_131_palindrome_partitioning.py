## 131. Palindrome Partitioning
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#     Input: "aab"
#     Output:
#     [
#         ["aa","b"],
#         ["a","a","b"]
#     ]
##


## dfs approach
## https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        print(list(s))
        if len(s) == 1:
            return [s]

        result = []
        temp_arr = list(s)

        for element in temp_arr:
            temp_result = True
            if not self.isPalindrome(element):
                temp_result = False
                return

        if temp_result:
            result.append(temp_arr)


        for i in range(len(temp_arr)-1):
            if self.isPalindrome(s[i] + s[i+1]):
                result.append(self.partition(s[i] + s[i+1]))

        return result


    def isPalindrome(self, str1):
        if len(str1) == 1:
            return True
        i = 0
        print(str1)
        while i < len(str1)-1-i:
            if str1[i] != str1[len(str1)-1-i]:
                return False
            i += 1
        return True


class Solution2(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    str1 = "aab"
    print(Solution2().partition(str1))