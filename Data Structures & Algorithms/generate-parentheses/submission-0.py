class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def b(open_n, closed_n, path):
            if open_n == closed_n == n:
                res.append(path)
                return
            
            if open_n < n:
                b(open_n + 1, closed_n, path + "(")

            if closed_n < open_n:
                b(open_n, closed_n + 1, path + ")")
        
        b(0, 0, "")
        
        return res
