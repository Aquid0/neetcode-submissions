class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.curr = []
        nums = sorted(nums)

        def f(start):
            self.ans.append(self.curr[::])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: # seen all these permutations already
                    continue
                
                self.curr.append(nums[i])
                f(i + 1)
                d = self.curr.pop()
        
        f(0)

        return self.ans