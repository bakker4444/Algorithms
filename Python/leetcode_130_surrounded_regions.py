## 130. Surrounded Regions
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
#     X X X X
#     X O O X
#     X X O X
#     X O X X
#
# After running your function, the board should be:
#
#     X X X X
#     X X X X
#     X X X X
#     X O X X
#
# Explanation:
#     Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
##



## approach 1
## DFS solution
## reference : https://leetcode.com/problems/surrounded-regions/discuss/41612/A-really-simple-and-readable-C++-solutiononly-cost-12ms
## time complexity : O(M*N)
## be careful about stack overflow for call-stack
## BFS might be other solution
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) < 3 or len(board[0]) < 3:
            return

        for i in range(len(board)):
            self.check(board, i, 0)
            if len(board[0]) > 1:
                self.check(board, i, len(board[0])-1)

        for j in range(1, len(board[0])-1):
            self.check(board, 0, j)
            if len(board) > 1:
                self.check(board, len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "1":
                    board[i][j] = "O"

    def check(self, board, x, y):
        if board[x][y] == "O":
            board[x][y] = "1"
            if x > 1:
                self.check(board, x-1, y)
            if y > 1:
                self.check(board, x, y-1)
            if x < len(board)-1:
                self.check(board, x+1, y)
            if y < len(board[0])-1:
                self.check(board, x, y+1)



from pprint import pprint
if __name__ == "__main__":
    inArr = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    Solution().solve(inArr)
    pprint(inArr)

    inArr = [
        ["X","O","X","X"],
        ["O","X","O","X"],
        ["X","O","X","O"],
        ["O","X","O","X"],
        ["X","O","X","O"],
        ["O","X","O","X"]
    ]
    Solution().solve(inArr)
    pprint(inArr)