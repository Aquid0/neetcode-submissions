from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        sort = sorted(x, key=x.get, reverse=True)
        return sort[:k]
        