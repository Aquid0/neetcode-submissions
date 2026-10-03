class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = stones
        heapq.heapify_max(h)

        while len(h) > 1:
            x = heapq.heappop_max(h)
            y = heapq.heappop_max(h)
            
            if x != y: 
                heapq.heappush_max(h, abs(y - x))
        
        return h[0] if h else 0