class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def f(curr, remaining):
            if len(curr) == len(nums):
                self.ans.append(curr[::])
            else:
                for i in range(len(remaining)):
                    f(curr + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        f([], nums)

        return self.ans