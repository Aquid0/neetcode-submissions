from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardLength = 9
        # Check rows
        for row in range(boardLength):
            count = defaultdict(int)
            for col in range(boardLength):
                boardVal = board[row][col]
                if boardVal.isnumeric():
                    count[boardVal] += 1
                    if count[boardVal] > 1:
                        return False

        # Check columns
        for col in range(boardLength):
            count = defaultdict(int)
            for row in range(boardLength):
                boardVal = board[row][col]
                if boardVal.isnumeric():
                    count[boardVal] += 1
                    if count[boardVal] > 1:
                        return False

        # Check subboxes
        for rowBox in range(0, boardLength, 3):
            for colBox in range(0, boardLength, 3):
                count = defaultdict(int)
                for row in range(rowBox, rowBox+3):
                    for col in range(colBox, colBox+3):
                        boardVal = board[row][col]
                        if boardVal.isnumeric():
                            count[boardVal] += 1
                            if count[boardVal] > 1:
                                return False
        return True
