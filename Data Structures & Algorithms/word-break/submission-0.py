class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * len(s) # Is it possible to segment from this index onwards?

        def dfs(i):
            if i >= len(s):
                return True

            if dp[i] is not None:
                return dp[i]

            branch = []

            for w in wordDict:
                if i + len(w) > len(s): # word is bigger than the segment we're trying to fit in
                    continue
                elif s[i : i + len(w)] == w: # word matches our segment
                    branch.append(dfs(i + len(w)))

            dp[i] = any(branch)
            
            return dp[i]
        
        dfs(0)

        return dp[0]


