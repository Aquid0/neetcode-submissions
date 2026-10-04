class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {i : None for i in range(1, n + 1)}

        def dfs(steps):
            if steps < 0: 
                return 0
            elif steps == 0: 
                return 1

            if steps - 1 in dp and dp[steps - 1] is not None:
                left = dp[steps - 1]
            else: 
                left = dfs(steps - 1)

            if steps - 2 in dp and dp[steps - 2] is not None:
                right = dp[steps - 2]
            else: 
                right = dfs(steps - 2)

            dp[steps] = left + right
            
            return left + right
        
        dfs(n)
        
        return dp[n]