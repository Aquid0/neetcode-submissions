class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(word)
        rows = len(board)
        cols = len(board[0])

        def b(seen, curr, path):
            r, c = curr 

            if len(path) > n: return False # not found
            if r >= rows: return False
            if r < 0: return False
            if c >= cols: return False
            if c < 0: return False
            if curr in seen: return False
            
            seen.add(curr)
            path += board[r][c]
            
            if path == word:
                return True

            f = (b(seen, (r + 1, c), path) or 
                    b(seen, (r - 1, c), path) or 
                    b(seen, (r, c + 1), path) or 
                    b(seen, (r, c - 1), path))

            seen.remove(curr)
 
            return f 

            
        for r in range(rows):
            for c in range(cols):
                t = b(set(), (r, c), "")
                if t:
                    return True
        
        return False