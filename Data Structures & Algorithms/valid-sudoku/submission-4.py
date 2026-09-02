class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidSet(arr):
            emptiedArr = list(filter(lambda x: x != ".", arr))
            return len(set(emptiedArr)) == len(emptiedArr)

        n = 9
        m = 9

        for row in range(n):
            if not isValidSet(board[row]):
                return False
        
        columns = [[row[i] for row in board] for i in range(n)]

        for column in columns:
            if not isValidSet(column):
                return False

        for r in range(0, n, 3):
            for c in range(0, m, 3):

                box = []
                for row in range(r, r+3):
                    for col in range(c, c+3):
                        box.append(board[row][col])
                        
                if not isValidSet(box):
                    return False

        return True        
