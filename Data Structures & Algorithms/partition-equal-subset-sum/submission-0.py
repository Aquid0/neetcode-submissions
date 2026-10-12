class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Brute force:

        Find every subset of nums, e.g. nums = [1,2,3,4], subset = [1, 4]:
        if sum(nums) - sum(subset) == sum(subset): the other subset equals this subset, then true


        i just need to find some subset of nums such that sum(nums) - sum(subset) == sum(subset)
        """

        dp = [0] * len(nums)
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        target = s / 2

        def dfs(i, curr):
            if curr == target:
                return True
            
            if i >= len(nums):
                return False
            
            if dp[i] != 0:
                return dp[i]
            
            seen = []
            for j in range(i + 1, len(nums)):
                if curr + nums[j] <= target: 
                    seen.append(dfs(j, curr + nums[j]))
            
            dp[i] = any(seen)
            
            return dp[i]
        
        dfs(0, 0)
        
        return any(dp)