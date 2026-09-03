from collections import Counter

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        x = Counter(nums)
        filteredNums = []

        for key, value in x.items():
            if value >= 3:
                filteredNums += [key] * 3
            else: 
                filteredNums += [key] * value

        n = len(filteredNums)

        for i in range(n):
            target = -filteredNums[i]
            seen = {}
            for j in range(i + 1, n):
                if target - filteredNums[j] in seen:
                    toAdd = tuple(sorted([filteredNums[i], filteredNums[j], target-filteredNums[j]]))
                    res.add(toAdd)
                seen[filteredNums[j]] = j
        
        
        return list([[i, j, k] for i, j, k in res])