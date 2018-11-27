## 79. Word Search
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
#     board =
#     [
#         ['A','B','C','E'],
#         ['S','F','C','S'],
#         ['A','D','E','E']
#     ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
##


## dfs approach
## key point : restore the board when recursive call return the result
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.isWordExist(word, board, x, y):
                    return True
        return False


    def isWordExist(self, word, board, x, y):
        if len(word) == 0:
            return True
        if x < 0 or x > len(board)-1 or y < 0 or y > len(board[0])-1:
            return False
        if word[0] != board[x][y]:
            return False

        temp = board[x][y]
        board[x][y] = ""
        ## North-South-East-West direction check
        temp_result = self.isWordExist(word[1:], board, x-1, y) \
            or self.isWordExist(word[1:], board, x+1, y) \
            or self.isWordExist(word[1:], board, x, y-1) \
            or self.isWordExist(word[1:], board, x, y+1)

        board[x][y] = temp

        return temp_result


if __name__ == "__main__":
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"
    print(Solution().exist(board, word))

    word = "SEE"
    print(Solution().exist(board, word))

    word = "ABCB"
    print(Solution().exist(board, word))

    board = [['A']]
    word = "A"
    print(Solution().exist(board, word))