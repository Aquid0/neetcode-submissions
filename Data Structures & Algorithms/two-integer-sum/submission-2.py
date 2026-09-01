class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in seen:
                return sorted([i, seen[ans]])
            seen[nums[i]] = i

        return []