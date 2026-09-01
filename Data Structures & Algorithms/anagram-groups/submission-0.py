class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort within each word, and then convert into a set
        # mlogm + nlogn
        # I will get all the base version of all the anagrams
        
        # then iterate throguh strs, sort the word and see if it exists in one of the anagrams
        # if it does, add to dict[str]
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = sorted(word)
            key = "".join(sorted_word)
            anagram_map[key].append(word)
            
        return list(anagram_map.values())