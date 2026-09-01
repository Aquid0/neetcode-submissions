class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        strsCopy = strs[::]
        ans = []

        for i in range(len(strs)):
            strsCopy[i] = ''.join(sorted(strs[i]))
            if strsCopy[i] in seen:
                seen[strsCopy[i]].append(i)
            else: 
                seen[strsCopy[i]] = [i]
        
        for anagram, indices in seen.items():
            subAns = []
            for i in indices:
                subAns.append(strs[i])
            ans.append(subAns)

        return ans
