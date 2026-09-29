class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            l = [nums[-1]]
            r = self.subsets(nums[:len(nums) - 1])
            return [x + l for x in r] + r