class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        comp = {}
        
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            seen[s2[i]] = seen.get(s2[i], 0) + 1
            comp[s1[i]] = comp.get(s1[i], 0) + 1
        
        if seen == comp:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            if seen[s2[i - 1]] > 1:
                seen[s2[i - 1]] -= 1
            else: 
                del seen[s2[i - 1]]

            seen[s2[i + len(s1) - 1]] = seen.get(s2[i + len(s1) - 1], 0) + 1

            if seen == comp:
                return True
                
        return False
            