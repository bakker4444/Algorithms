## 14. Longest Common Prefix
#
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]

        minWord = strs[0]
        # Find min length word
        for word in strs:
            if len(word) < len(minWord):
                minWord = word

        result = ""

        for end in range(len(minWord)):
            flagCount = 0

            for word in strs:

                if minWord[:len(minWord)-end] == word[:len(minWord)-end]:
                    flagCount += 1
                    continue
                else:
                    break
            if flagCount == len(strs):
                result = minWord[:len(minWord)-end]
                break

        return result


## test
if __name__ == "__main__":
    input = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(input))
    input = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(input))
    input = ["ca", "a"]
    print(Solution().longestCommonPrefix(input))
    input = ["b", "a"]
    print(Solution().longestCommonPrefix(input))
