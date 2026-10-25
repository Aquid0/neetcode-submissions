class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None] * len(nums)
        
        if len(nums) == 1:
            return True

        if not nums[0]:
            return False

        def dfs(i):
            if i >= len(nums) - 1: 
                return True
            
            if nums[i] == 0:
                return False

            if dp[i] is not None:
                return dp[i]
            
            res = []
            jumps = nums[i]

            for j in range(jumps):
                res.append(dfs(i + j + 1))
            
            dp[i] = any(res)
        
            return dp[i]
        
        dfs(0)

        return dp[0]
                                            

            


                
        
                    