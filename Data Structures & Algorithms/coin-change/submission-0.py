class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        if amount == 0:
            return 0

        def dfs(i): 
            if i < 0: 
                return float('inf')
            
            if i == 0:
                return 1
            
            if i in dp:
                return dp[i]

            m = float('inf')
            for n in coins: 
                m = min(m, dfs(i - n))
        
            dp[i] = 1 + m

            return 1 + m
        
        dfs(amount)

        return dp[amount] - 1 if dp[amount] != float('inf') else -1
