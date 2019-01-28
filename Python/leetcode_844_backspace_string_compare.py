## 844. Backspace String Compare
#
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#     Input: S = "ab#c", T = "ad#c"
#     Output: true
#     Explanation: Both S and T become "ac".
#
# Example 2:
#     Input: S = "ab##", T = "c#d#"
#     Output: true
#     Explanation: Both S and T become "".
#
# Example 3:
#     Input: S = "a##c", T = "#a#c"
#     Output: true
#     Explanation: Both S and T become "c".
#
# Example 4:
#     Input: S = "a#c", T = "b"
#     Output: false
#     Explanation: S becomes "c" while T becomes "b".
#
# Note:
#     1) 1 <= S.length <= 200
#     2) 1 <= T.length <= 200
#     3) S and T only contain lowercase letters and '#' characters.
#
# Follow up:
#     Can you solve it in O(N) time and O(1) space?
##


## reference : https://leetcode.com/problems/backspace-string-compare/discuss/161771/Python-O(1)-Space
## time complexity : O(N)
## space complexity : O(1)
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sIdx = len(S)-1
        tIdx = len(T)-1
        bspace_count_s = 0
        bspace_count_t = 0

        while sIdx >= 0 or tIdx >= 0:

            #find character in s
            while sIdx >= 0:
                if S[sIdx] == "#":
                    sIdx -= 1
                    bspace_count_s += 1
                else:    # S[sIdx] != "#":
                    if bspace_count_s > 0:
                        sIdx -= 1
                        bspace_count_s -= 1
                    else:
                        break

            while tIdx >= 0:
                if T[tIdx] == "#":
                    tIdx -= 1
                    bspace_count_t += 1
                else:    # T[tIdx] != "#"
                    if bspace_count_t > 0:
                        tIdx -= 1
                        bspace_count_t -= 1
                    else:
                        break

            if (sIdx < 0 and tIdx >= 0) or (sIdx >= 0 and tIdx < 0):
                return False

            if (sIdx >= 0 and tIdx >= 0) and (S[sIdx] != T[tIdx]):
                return False

            sIdx -= 1
            tIdx -= 1

        return True



if __name__ == "__main__":
    print(Solution().backspaceCompare("ab#c", "ad#c"))
    print(Solution().backspaceCompare("ab##", "c#d#"))
    print(Solution().backspaceCompare("a##c", "#a#c"))
    print(Solution().backspaceCompare("a#c", "b"))