## 242. Valid Anagram
#
# Given two strings s and t , write a function to determine if t is an anagram of s.
#
#     Example 1:
#         Input: s = "anagram", t = "nagaram"
#         Output: true
#
#     Example 2:
#         Input: s = "rat", t = "car"
#         Output: false
#
# Note:
#     You may assume the string contains only lowercase alphabets.
#
# Follow up:
#     What if the inputs contain unicode characters? How would you adapt your solution to such case?
##



## dictionary
## time complexity : O(N)
## space complexity : O(N)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic = {}

        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

        for ch in t:
            if (ch not in dic) or (ch in dic and dic[ch] <= 0):
                return False
            dic[ch] -= 1

        return True



import unittest
class Test(unittest.TestCase):
    def test_isAnagram(self):
        test_input = [
            ["anagram", "nagaram"]
        ]
        test_output = [
            True
        ]
        for i in range(len(test_input)):
            result = Solution().isAnagram(test_input[i][0], test_input[i][1])
            self.assertEqual(result, test_output[i])



if __name__ == "__main__":
    unittest.main()

