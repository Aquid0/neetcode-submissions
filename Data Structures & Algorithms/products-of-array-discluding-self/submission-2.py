class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        forward = nums[::]
        backward = nums[::]

        for i in range(1, n):
            forward[i] *= forward[i-1] 
        
        for i in range(n-2, -1, -1):
            backward[i] *= backward[i+1]

        ans = [1 for i in range(n)]

        ans[0] = backward[1]
        ans[-1] = forward[n-2]
        
        for i in range(1, n-1): 
            ans[i] = forward[i-1] * backward[i+1]

        return ans

        

