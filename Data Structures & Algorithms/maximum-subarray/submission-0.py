class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        iterate through, collecting the sum
        ans = max(ans, curr)

        if the sum becomes negative, we should not add this current subarray to any other subarray, so we start a new sum
        if curr < 0:
            curr = 0
        """

        ans = float('-inf')
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]
            ans = max(ans, curr)

            if curr < 0:
                curr = 0
            
        
        return ans