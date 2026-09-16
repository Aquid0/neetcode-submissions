class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isEqualCount(x, y):
            for letter in y:
                if letter not in x:
                    return False

                if x[letter] < y[letter]:
                    return False
        
            return True

        l = 0
        seen = {} 
        comp = Counter(t)

        minLength = float("inf")
        bestRange = (-1, -1)

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            
            while isEqualCount(seen, comp):
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    bestRange = (l, r)

                if seen[s[l]] == 1:
                    del seen[s[l]]
                else:
                    seen[s[l]] -= 1
                
                l += 1
    
        start, end = bestRange
        ans = s[start : end + 1]

        return ans if len(ans) != float("inf") else ""


            
