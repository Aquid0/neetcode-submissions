class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        search = {nums[i] : i for i in range(n)}
        largestNums = []
        allSeqs = []

        for num in nums:
            if num+1 in search:
                continue
            else:
                largestNums.append(num)

        for topSeq in range(len(largestNums)):
            val = largestNums[topSeq]
            hasMore = True
            curr = 1
            while hasMore:
                if val - 1 in search:
                    curr += 1
                    val = val - 1
                else: 
                    hasMore = False
            allSeqs.append(curr)

        if len(allSeqs) == 0:
            return 0

        return max(allSeqs)
            

            
