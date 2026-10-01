class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        x = { 
            "2" : "abc", 
            "3" : "def", 
            "4" : "ghi", 
            "5" : "jkl", 
            "6" : "mno", 
            "7" : "pqrs", 
            "8" : "tuv", 
            "9" : "wxyz"
        }
        ans = []

        def dfs(i, path):
            if i >= len(digits):
                ans.append(path)
                return
            
            digitChar = digits[i]

            for l in x[digitChar]:
                dfs(i + 1, path + l)
        
        dfs(0, "")
        
        return ans

                
            