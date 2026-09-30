class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        def f(l): 
            if len(l) == 0:
                return [[]]
            else: 
                last = [nums[-1]]
                r = self.subsetsWithDup(nums[:len(nums) - 1])

                out = []

                for listItem in r:
                    if last[0] not in listItem:
                        out.append(listItem)
                
                return [x + last for x in r] + out
        
        return f(nums)