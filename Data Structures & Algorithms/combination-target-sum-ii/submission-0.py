class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        nums = sorted(candidates)

        def f(curr, target, start):
            if target == 0:
                self.ans.append(list(curr))
                return
            else: 
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i - 1]: 
                        continue

                    num = nums[i]

                    if target - num < 0:
                        break
                    
                    curr.append(num)
                    f(curr, target - num, i + 1)
                    curr.pop()
        
        f([], target, 0)

        return self.ans