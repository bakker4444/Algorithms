## 36. Valid Sudoku
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
#     [5] [3] [ ] | [ ] [7] [ ] | [ ] [ ] [ ]
#     [6] [ ] [ ] | [1] [9] [5] | [ ] [ ] [ ]
#     [ ] [9] [8] | [ ] [ ] [ ] | [ ] [6] [ ]
#     ---------------------------------------
#     [8] [ ] [ ] | [ ] [6] [ ] | [ ] [ ] [3]
#     [4] [ ] [ ] | [8] [ ] [3] | [ ] [ ] [1]
#     [7] [ ] [ ] | [ ] [2] [ ] | [ ] [ ] [6]
#     ---------------------------------------
#     [ ] [6] [ ] | [ ] [ ] [ ] | [2] [8] [ ]
#     [ ] [ ] [ ] | [4] [1] [9] | [ ] [ ] [5]
#     [ ] [ ] [ ] | [ ] [8] [ ] | [ ] [7] [9]
#
#     A partially filled sudoku which is valid.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# Example 1:
#
#     Input:
#     [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
#     ]
#     Output: true
#
# Example 2:
#
#     Input:
#     [
#     ["8","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
#     ]
#     Output: false
#     Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
# Note:
#
#     - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     - Only the filled cells need to be validated according to the mentioned rules.
#     - The given board contain only digits 1-9 and the character '.'.
#     - The given board size is always 9x9.
##


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for rowNum in range(len(board)):
            for colNum in range(len(board[rowNum])):

                element = board[rowNum][colNum]

                if element == ".":
                    continue

                element = 1 << int(element) - 1

                if element & rows[rowNum]:
                    return False
                if element & cols[colNum]:
                    return False
                if element & squares[(rowNum//3)*3 + colNum//3]:
                    return False

                rows[rowNum] |= element
                cols[colNum] |= element
                squares[(rowNum//3)*3 + colNum//3] |= element

        return True


if __name__ =="__main__":
    arr1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(Solution().isValidSudoku(arr1))
    arr1 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(Solution().isValidSudoku(arr1))
