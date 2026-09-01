from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardLength = 9

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(boardLength):
            for col in range(boardLength):
                val = board[row][col]

                if val == ".":
                    continue
                
                box_idx = (row // 3) * 3 + (col // 3)

                if val in rows[row] or val in cols[col] or val in boxes[box_idx]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                boxes[box_idx].add(val)

        return True
