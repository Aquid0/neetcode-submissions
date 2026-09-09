class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2

            if nums[r] <= nums[mid]: # if num at mid is greater than r, then the min is to the right
                l = mid + 1
            else: # nums between l and m are not sorted, so pivot point must be to the left
                r = mid
    
        return nums[r]