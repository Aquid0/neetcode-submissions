class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist_sq = -(x * x + y * y)
            
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist_sq, x, y))
            else:
                heapq.heappushpop(max_heap, (dist_sq, x, y))

        return [[x, y] for (_, x, y) in max_heap]