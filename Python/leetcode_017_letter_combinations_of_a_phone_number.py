## 17. Letter Combinations of a Phone Number
#
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#                 2 : "abc"   3 : "def"
#     4 : "ghi"   5 : "jkl"   6 : "mno"
#     7 : "pqrs"  8 : "tuv"   9 : "wxyz"
#
# Example:
#     Input: "23"
#     Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
# Note:
#     Although the above answer is in lexicographical order, your answer could be in any order you want.
##


## iterative approach
# time complexity : O(3^N * 4^M)
# space complexity : O(3^N * 4^M)
#       - N: numver of digits that maps to 3 characters
#       - M: numver of digits tha maps to 4 characters
class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []

        if not digits:
            return result

        temp = lookup[digits[0]]
        idx = 1
        i, j = 0, 0

        while idx < len(digits):
            temp2 = lookup[digits[idx]]
            for i in range(len(temp)):
                for j in range(len(temp2)):
                    result.append(temp[i] + temp2[j])
            idx += 1
            temp = result
            result = []

        return temp


## recursive approach, backtracking
# time complexity : O(3^N * 4^M)
# space complexity : O(3^N * 4^M)
#       - N: numver of digits that maps to 3 characters
#       - M: numver of digits tha maps to 4 characters
class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def helper(combi, next_num):
            if len(next_num) == 0:
                return result.append(combi)
            else:
                for character in lookup[next_num[0]]:
                    helper(combi + character, next_num[1:])

        result = []
        if digits:
            helper("", digits)
        return result


## recursive approach
# time complexity : O(3^N * 4^M)
# space complexity : O(3^N * 4^M)
#       - N: numver of digits that maps to 3 characters
#       - M: numver of digits tha maps to 4 characters
class Solution3(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        self.dfs(digits, lookup, 0, "", result)
        return result

    def dfs(self, digits, dic, idx, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in range(idx, len(digits)):
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i+1, path+j, res)






import unittest
class Test(unittest.TestCase):
    def test_letterCombinations(self):
        test_input = [
            "23",
            "485"
        ]
        test_output = [
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
            ["gtj","gtk","gtl","guj","guk","gul","gvj","gvk","gvl","htj","htk","htl","huj","huk","hul","hvj","hvk","hvl","itj","itk","itl","iuj","iuk","iul","ivj","ivk","ivl"]
        ]
        for i in range(len(test_input)):
            result1 = Solution1().letterCombinations(test_input[i])
            result2 = Solution2().letterCombinations(test_input[i])
            result3 = Solution3().letterCombinations(test_input[i])
            self.assertEqual(result1, test_output[i])
            self.assertEqual(result2, test_output[i])
            self.assertEqual(result3, test_output[i])
            print(result1)
            print(result2)
            print(result3)



if __name__ == "__main__":
    unittest.main()