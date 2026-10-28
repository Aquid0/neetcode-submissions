class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        
        if len(nums) == 1:
            return 0

        def dfs(i):
            if i >= len(nums) - 1: 
                return 0
            
            if nums[i] == 0:
                return float("inf")

            if dp[i] is not None:
                return dp[i]
            
            jumps = nums[i]
            max_jump = min(nums[i], len(nums) - 1 - i)
            res = float("inf")

            for j in range(max_jump, 0, -1):
                res = min(res, dfs(i + j))
            
            dp[i] = 1 + res

            return dp[i]
        
        dfs(0)

        return dp[0]
                            