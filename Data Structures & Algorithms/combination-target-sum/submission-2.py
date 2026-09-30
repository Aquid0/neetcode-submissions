class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        nums = sorted(nums)

        def f(curr, target, start):
            if target == 0:
                self.ans.append(list(curr))
                return
            else: 
                for i in range(start, len(nums)):
                    num = nums[i]

                    if target - num < 0: 
                        break
                    
                    curr.append(num)
                    f(curr, target - num, i)
                    curr.pop()

        
        f([], target, 0)

        return self.ans
