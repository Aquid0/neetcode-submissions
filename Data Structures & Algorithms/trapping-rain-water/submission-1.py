class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        
        leftMax = [1 for _ in range(n)]
        leftMaxCurr = -1

        rightMax = [1 for _ in range(n)]
        rightMaxCurr = -1

        for i in range(n):
            leftMaxCurr = max(leftMaxCurr, height[i])
            leftMax[i] = leftMaxCurr
        
        for i in range(n-1, -1, -1):
            rightMaxCurr = max(rightMaxCurr, height[i])
            rightMax[i] = rightMaxCurr
        
        for i in range(1, n-1):
            ans += max(0, min(leftMax[i], rightMax[i]) - height[i])
        
        return ans