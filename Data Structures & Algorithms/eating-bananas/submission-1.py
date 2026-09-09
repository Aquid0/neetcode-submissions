import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 1000000000

        def checkEatingRate(k):
            res = 0
            for p in piles:
                res += math.ceil(p / k)
            return res <= h
        
        while l <= r: 
            mid = (l + r) // 2

            if checkEatingRate(mid):
                r = mid - 1
            else: 
                l = mid + 1
        
        return l
        

