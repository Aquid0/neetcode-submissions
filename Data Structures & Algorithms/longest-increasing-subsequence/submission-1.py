class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        def dfs(i):
            if dp[i] != 0:
                return dp[i]
            
            curr = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    curr = max(curr, dfs(j))
            
            dp[i] = 1 + curr
            return dp[i]
    
        dfs(0)

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))

        return ans