class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for fixed_idx in range(n):
            seen = {}
            target = 0 - nums[fixed_idx]
            for outer in range(n): 
                if outer == fixed_idx:
                    continue
                if target - nums[outer] in seen:
                    triplet = tuple(sorted((nums[fixed_idx], nums[outer], target-nums[outer])))
                    ans.add(triplet)
                seen[nums[outer]] = outer
        
        return [list(item) for item in ans]                     