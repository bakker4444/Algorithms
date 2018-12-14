## 395. Longest Substring with At Least K Repeating Characters
#
# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
#
# Example 1:
#     Input:  s = "aaabb", k = 3
#     Output: 3
#
#     The longest substring is "aaa", as 'a' is repeated 3 times.
#
# Example 2:
#     Input:  s = "ababbc", k = 2
#     Output: 5
#
#     The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
##


## recursive approach
## reference
## https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87736/C++-recursive-solution
"""
1. in the first pass I record counts of every character in a hashmap
2. in the second pass I locate the first character that appear less than k times in the string. this character is definitely not included in the result, and that separates the string into two parts.
3. keep doing this recursively and the maximum of the left/right part is the answer.
"""
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        record = dict()
        for i in range(len(s)):
            if s[i] not in record:
                record[s[i]] = 1
            else:
                record[s[i]] += 1
        idx = 0
        while idx < len(s) and record[s[idx]] >= k:
            idx += 1
        if idx == len(s):
            return len(s)
        left = self.longestSubstring(s[:idx], k)
        right = self.longestSubstring(s[idx+1:], k)
        return max(left, right)


if __name__ == "__main__":
    s = "aaabb"
    k = 3
    print(Solution().longestSubstring(s, k))
    s = "ababbc"
    k = 2
    print(Solution().longestSubstring(s, k))
    s = "ababacb"
    k = 3
    print(Solution().longestSubstring(s, k))
