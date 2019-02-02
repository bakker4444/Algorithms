## 127. Word Ladder
#
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#     1. Only one letter can be changed at a time.
#     2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
# Note:
#     * Return 0 if there is no such transformation sequence.
#     * All words have the same length.
#     * All words contain only lowercase alphabetic characters.
#     * You may assume no duplicates in the word list.
#     * You may assume beginWord and endWord are non-empty and are not the same.
#
# Example 1:
#     Input:
#         beginWord = "hit",
#         endWord = "cog",
#         wordList = ["hot","dot","dog","lot","log","cog"]
#     Output: 5
#
#     Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
#
# Example 2:
#     Input:
#         beginWord = "hit"
#         endWord = "cog"
#         wordList = ["hot","dot","dog","lot","log"]
#     Output: 0
#
#     Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
##



## reference : https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
## time complexity : O(L*26*N), for L:length of a word, N:number of words
## space complexity : O(N) for deque size
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = deque([(beginWord, 1)])

        while queue:
            word, dist = queue.popleft()

            ## termination condition
            if word == endWord:
                return dist

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    temp_word = word[:i] + c + word[i+1:]

                    if temp_word in wordList:
                        wordList.remove(temp_word)
                        queue.append((temp_word, dist+1))

        return 0



import unittest
class Test(unittest.TestCase):
    def test_ladderLength(self):
        test_inputs = [
            ["hit", "cog", ["hot","dot","dog","lot","log","cog"]],
            ["hit", "cog", ["hot","dot","dog","lot","log"]],
        ]
        test_result = [5, 0]

        for i in range(len(test_inputs)):
            result = Solution().ladderLength(test_inputs[i][0], test_inputs[i][1], test_inputs[i][2])
            self.assertEqual(result, test_result[i])
            print(result)


if __name__ == "__main__":
    unittest.main()