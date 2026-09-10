class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l1 = 0
        r1 = len(nums) - 1
        k = -1

        while l1 < r1:
            mid1 = (l1 + r1) // 2
        
            if nums[r1] <= nums[mid1]:
                l1 = mid1 + 1
            else: 
                r1 = mid1
    
        k = r1 # how much we're rotated by

        l2 = 0
        r2 = k - 1

        while l2 <= r2:
            mid2 = (l2 + r2) // 2

            if nums[mid2] == target:
                return mid2
            elif nums[mid2] < target:
                l2 = mid2 + 1
            else:
                r2 = mid2 - 1

        l3 = k
        r3 = len(nums) - 1

        while l3 <= r3:
            mid3 = (l3 + r3) // 2

            if nums[mid3] == target:
                return mid3
            elif nums[mid3] < target:
                l3 = mid3 + 1
            else:
                r3 = mid3 - 1

        return -1
        
        
        
        
        
        
