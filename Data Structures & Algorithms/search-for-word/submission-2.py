class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        rows = len(board)
        cols = len(board[0])

        def b(curr, path):
            r, c = curr 

            if r >= rows or r < 0 or c >= cols or c < 0: return False
            if board[r][c] == '#': return False

            if board[r][c] != word[path]: 
                return False
            
            if path == n - 1: 
                return True
            
            t = board[r][c]
            board[r][c] = '#'

            f = (b((r + 1, c), path + 1) or 
                    b((r - 1, c), path + 1) or 
                    b((r, c + 1), path + 1) or 
                    b((r, c - 1), path + 1))
 
            board[r][c] = t

            return f 

            
        for r in range(rows):
            for c in range(cols):
                t = b((r, c), 0)
                if t:
                    return True
        
        return False