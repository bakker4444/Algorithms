## 830. Positions of Large Groups
#
# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#
# The final answer should be in lexicographic order.
#
#
# Example 1:
#
#     Input: "abbxxxxzzy"
#     Output: [[3,6]]
#     Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
#
# Example 2:
#
#     Input: "abc"
#     Output: []
#     Explanation: We have "a","b" and "c" but no large group.
#
# Example 3:
#
#     Input: "abcdddeeeeaabbbcd"
#     Output: [[3,5],[6,9],[12,14]]
#
# Note:  1 <= S.length <= 1000
##


# ## approach 2: two pointer
# class Solution(object):
#     def largeGroupPositions(self, S):
#         """
#         :type S: str
#         :rtype: List[List[int]]
#         """
#         result = []
#         start_idx = 0
#         for i in range(len(S)):
#             if i == len(S)-1 or S[i] != S[i+1]:
#                 if i - start_idx + 1 >= 3:
#                     result.append([start_idx, i])
#                 start_idx = i + 1
#         return result


# approach 1: my solution
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if not S:
            return []
        if len(S) < 3:
            return []
        start_idx = 0
        str_len = 1
        result = []
        for i in range(1, len(S)):
            if S[i] != S[i-1]:
                if str_len >= 3:
                    result.append([start_idx, start_idx+str_len-1])
                start_idx = i
                str_len = 1
            else:
                str_len += 1
            if i == len(S)-1 and str_len >= 3:
                result.append([start_idx, start_idx+str_len-1])
        return result


if __name__ == "__main__":
    str1 ="abbxxxxzzy"
    print(Solution().largeGroupPositions(str1))
    str1 = "abc"
    print(Solution().largeGroupPositions(str1))
    str1 = "abcdddeeeeaabbbcd"
    print(Solution().largeGroupPositions(str1))
    str1 = "aaa"
    print(Solution().largeGroupPositions(str1))
    str1 = "aaaa"
    print(Solution().largeGroupPositions(str1))