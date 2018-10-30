## 3. Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
#     Input: "abcabcbb"
#     Output: 3
#     Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
#     Input: "bbbbb"
#     Output: 1
#     Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
#     Input: "pwwkew"
#     Output: 3
#     Explanation: The answer is "wke", with the length of 3.
#                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
##


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        starting_idx = 0
        max_length = 0
        character_check = {}

        for i in range(len(s)):
            if s[i] in character_check and starting_idx <= character_check[s[i]]:
                starting_idx = character_check[s[i]] + 1
            else:
                max_length = max(max_length, i - starting_idx + 1)
            character_check[s[i]] = i

        return max_length


if __name__ == "__main__":
    str1 = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(str1))

    str1 = "bbbbb"
    print(Solution().lengthOfLongestSubstring(str1))

    str1 = "pwwkew"
    print(Solution().lengthOfLongestSubstring(str1))
