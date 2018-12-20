## 212. Word Search II
#
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example:
#
# Input:
#     words = ["oath","pea","eat","rain"] and
#     board = [
#         ['o','a','a','n'],
#         ['e','t','a','e'],
#         ['i','h','k','r'],
#         ['i','f','l','v']
#     ]
#
#     Output: ["eat","oath"]
#
# Note:
#     You may assume that all inputs are consist of lowercase letters a-z.
##


## reference
## https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for character in word:
            node = node.children[character]
        node.isWord = True

    def search(self, word):
        node = self.root
        for character in word:
            node = node.children.get(character)
            if not node:
                return False
        return self.isWord


class Solution1(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        trie = Trie()
        node = trie.root
        ## make trie for words array
        for word in words:
            trie.insert(word)

        ## search for word on board
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", result)
        return result

    def dfs(self, board, node, i, j, path, result):
        if node.isWord:
            result.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        temp = board[i][j]
        node = node.children.get(temp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+temp, result)
        self.dfs(board, node, i-1, j, path+temp, result)
        self.dfs(board, node, i, j+1, path+temp, result)
        self.dfs(board, node, i, j-1, path+temp, result)
        board[i][j] = temp


## reference
## https://leetcode.com/problems/word-search-ii/discuss/59864/Python-code-use-trie-and-dfs-380ms
class Solution2(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            t = trie
            for character in word:
                if character not in t:
                    t[character] = {}
                t = t[character]
            t["#"] = "#"
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie, "", result)
        return list(set(result))

    def find(self, board, i, j, trie, path, result):
        if "#" in trie:
            result.append(path)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie:
            return
        temp = board[i][j]
        board[i][j] = "@"
        self.find(board, i+1, j, trie[temp], path+temp, result)
        self.find(board, i-1, j, trie[temp], path+temp, result)
        self.find(board, i, j+1, trie[temp], path+temp, result)
        self.find(board, i, j-1, trie[temp], path+temp, result)
        board[i][j] = temp



if __name__ == "__main__":
    words = ["oath","pea","eat","rain"]
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    print(Solution1().findWords(board, words))
    print(Solution2().findWords(board, words))