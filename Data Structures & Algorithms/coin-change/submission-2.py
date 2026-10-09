class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = {}

        def dfs(i):
            if i == 0: return 0
            if i < 0: return float('inf')
            if i in dp: return dp[i]

            m = float('inf')
            for n in coins: 
                m = min(m, dfs(i - n))
            
            dp[i] = 1 + m

            return dp[i]
        
        ans = dfs(amount)

        return ans if ans != float('inf') else -1