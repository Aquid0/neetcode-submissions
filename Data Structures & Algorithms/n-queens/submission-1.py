class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []

        def dfs(c):
            if c >= n:
                ans.append(["".join(row) for row in board])
                return 
            
            for row in range(n):
                if isQueenValid(row, c):
                    board[row][c] = "Q"
                    dfs(c + 1)
                    board[row][c] = "."

        def isQueenValid(r, c):
            for i in range(1, c + 1):
                if board[r][c - i] == "Q":
                    return False
                if r - i >= 0 and board[r - i][c - i] == "Q":
                    return False
                if r + i < n and board[r + i][c - i] == "Q":
                    return False
            return True
            
        dfs(0)

        return ans