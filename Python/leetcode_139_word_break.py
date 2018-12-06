## 139. Word Break
#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
#     - The same word in the dictionary may be reused multiple times in the segmentation.
#     - You may assume the dictionary does not contain duplicate words.
#
# Example 1:
#
#     Input: s = "leetcode", wordDict = ["leet", "code"]
#     Output: true
#     Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Example 2:
#
#     Input: s = "applepenapple", wordDict = ["apple", "pen"]
#     Output: true
#     Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#                  Note that you are allowed to reuse a dictionary word.
# Example 3:
#
#     Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
#     Output: false
##



## reference
## https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways?page=1
##
## Example:
## s = "leetcode"
## words = ["leet", "code"]
## d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
## d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True
##
## Initial
##  result = [T, F, F, F, F, F, F, F, F]
##  i range : 1 ~ 8(inclusive)
##  j range : 0 ~ 7(inclusive)
##
## when hits i = 4, j = 0
##      result[j] = result[0] = True    <-- if previous_word exists in dictionary, in this case "", default True
##      search_word = s[j:i] = s[0:4] = "leet"
##      search_word in dictionary ==> result[i] = result[4] = True
##                               *
##                  [T, F, F, F, T, F, F, F, F]
##
## when hits i = 8, j = 4
##      result[j] = result[4] = True    <-- if previous_word exists in dictionary, in this case "leet"
##      search_word = s[j:i] = s[4:8] = "code"  <-- if later part of word, s[4:8]="code", also exists in dictionary
##      search_word in dictionary ==> result[i] = True  <-- then update result array
##                                           *
##                  [T, F, F, F, T, F, F, F, T]
##
## return result[-1]
class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        result = [False] * (len(s)+1)

        result[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if result[j]:
                    search_word = s[j:i]
                    if search_word in wordDict:
                        result[i] = True
                        break

        return result[-1]


## dynamic programming using word length, and memoization
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.walk(s, wordDict, 0, {})

    def walk(self, s, wordDict, pos, memo):
        if pos == len(s):
            return True
        elif pos > len(s):
            return False

        if pos in memo:
            return memo[pos]

        for word in wordDict:
            end = pos + len(word)
            if s[pos:end] == word:
                if self.walk(s, wordDict, end, memo):
                    memo[pos] = True
                    return memo[pos]

        memo[pos] = False
        return memo[pos]



if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution1().wordBreak(s, wordDict))
    print(Solution2().wordBreak(s, wordDict))

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(Solution1().wordBreak(s, wordDict))
    print(Solution2().wordBreak(s, wordDict))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution1().wordBreak(s, wordDict))
    print(Solution2().wordBreak(s, wordDict))

    s = "cars"
    wordDict = ["car","ca","rs"]
    print(Solution1().wordBreak(s, wordDict))
    print(Solution2().wordBreak(s, wordDict))

    s = "ccbb"
    wordDict = ["bc","cb"]
    print(Solution1().wordBreak(s, wordDict))
    print(Solution2().wordBreak(s, wordDict))
