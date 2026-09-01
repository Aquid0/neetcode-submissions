from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        cList = list(c.items())
        cListSorted = sorted(cList, key = lambda x: x[1], reverse=True)

        return [i[0] for i in cListSorted][:k]
        