class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for i in range(len(nums)):
            if len(h) >= k: 
                heapq.heappush(h, nums[i])
                heapq.heappop(h)
            else: 
                heapq.heappush(h, nums[i])
        
        return h[0]