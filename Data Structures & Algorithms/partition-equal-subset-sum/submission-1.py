class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s / 2
    
        def dfs(i, curr):
            if curr == target:
                return True 
            if i >= len(nums) or curr > target:
                return False
            
            if (i, curr) in dp:
                return dp[(i, curr)]
            
            res = dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr)
            dp[(i, curr)] = res
            return res
        
        return dfs(0, 0)
        