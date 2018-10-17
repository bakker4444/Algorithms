## 289. Game of Life
#
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
#
# Example:
#
#     Input:
#     [
#         [0,1,0],
#         [0,0,1],
#         [1,1,1],
#         [0,0,0]
#     ]
#
#     Output:
#     [
#         [0,0,0],
#         [1,0,1],
#         [0,1,1],
#         [0,1,0]
#     ]
#
# Follow up:
#
#     1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
#     2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
##


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        maxRow, maxCol = len(board), len(board[0])
        for row in range(maxRow):
            for col in range(maxCol):
                if board[row][col] == 0:    ## currently dead cell
                    if self.checkLiveOrDead(board, row, col) == 3:
                        board[row][col] = 2     ## will be alive
                else:       ## currently live cell
                    nearCellCount = self.checkLiveOrDead(board, row, col)
                    if nearCellCount < 2 or nearCellCount > 3:
                        board[row][col] = 3     ## will dead
        for row in range(maxRow):
            for col in range(maxCol):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == 3:
                    board[row][col] = 0

        print(board)



    def checkLiveOrDead(self, board, row, col):
        maxRow, maxCol = len(board), len(board[0])
        live = 0
        if row-1 >= 0 and col-1 >= 0:
            live += board[row-1][col-1]%2
        if row-1 >= 0:
            live += board[row-1][col]%2
        if row-1 >= 0 and col+1 < maxCol:
            live += board[row-1][col+1]%2
        if col-1 >= 0:
            live += board[row][col-1]%2
        if col+1 < maxCol:
            live += board[row][col+1]%2
        if row+1 < maxRow and col-1 >= 0:
            live += board[row+1][col-1]%2
        if row+1 < maxRow:
            live += board[row+1][col]%2
        if row+1 < maxRow and col+1 < maxCol:
            live += board[row+1][col+1]%2
        return live


if __name__ == "__main__":
    arr1 = [[0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]]
    print(Solution().gameOfLife(arr1))
    arr1 = [[1,1],
            [1,0]]
    print(Solution().gameOfLife(arr1))