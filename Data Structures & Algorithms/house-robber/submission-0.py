class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [float('-inf')] * (len(nums) + 1)
        s = 0
        nums = [0] + nums

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if dp[i] != float('-inf'):
                return dp[i]

            s = max(nums[i] + dfs(i + 2), dfs(i + 1))
            dp[i] = s

            return s
        
        dfs(0)

        return dp[0]