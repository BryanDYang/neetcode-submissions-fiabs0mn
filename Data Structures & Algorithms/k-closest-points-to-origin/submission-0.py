class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p[0], p[1]
            ed = math.sqrt(x**2 + y**2) 
            heap.append([ed, x, y])
        
        heapq.heapify(heap)
        
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1

        return res
        