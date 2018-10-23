## 125. Valid Palindrome
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
#     Input: "A man, a plan, a canal: Panama"
#     Output: true
#
# Example 2:
#
#     Input: "race a car"
#     Output: false
##


## approach 2: two index way
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or s == "":
            return True

        s = s.lower()
        left_idx = 0
        right_idx = len(s) - 1

        print(s)

        while left_idx < right_idx:
            while left_idx < right_idx and not s[left_idx].isalnum():
                left_idx += 1
            while left_idx < right_idx and not s[right_idx].isalnum():
                right_idx -= 1
            # print(s[left_idx], s[right_idx])
            if s[left_idx] != s[right_idx]:
                return False
            left_idx += 1
            right_idx -= 1
        return True


## approach 1: my approach
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if not s or s == "":
#             return True
#         str1 = ""
#         for character in s:
#             if character.isalnum():
#                 str1 += character.lower()
#         # print(str1)
#         for i in range(len(str1)//2):
#             # print(str1[i], str1[len(str1)-1-i])
#             if str1[i] != str1[len(str1)-1-i]:
#                 return False
#         return True


if __name__ == "__main__":
    str1 = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(str1))

    str1 = "race a car"
    print(Solution().isPalindrome(str1))
