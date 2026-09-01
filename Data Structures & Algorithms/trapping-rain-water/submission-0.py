class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxPref = [-1]
        leftMax = -1

        rightMaxPref = [-1]
        rightMax = -1

        n = len(height)
        water = 0

        for left in range(1, n):
            leftMax = max(leftMax, height[left-1])
            leftMaxPref.append(leftMax)
    
        for right in range(n-2, -1, -1):
            rightMax = max(rightMax, height[right+1])
            rightMaxPref.insert(0, rightMax)
        
        for i in range(n):
            left = leftMaxPref[i]
            right = rightMaxPref[i]
            h = height[i]

            if left > h and right > h:
                water += min(left, right) - h 

        return water 
