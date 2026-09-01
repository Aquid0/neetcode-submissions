from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)

        if len(counterS) != len(counterT): 
            return False

        for char, count in counterS.items():
            if counterT[char] != count:
                return False
        
        return True


        