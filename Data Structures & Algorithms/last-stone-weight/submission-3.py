class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            print(x)
            print(y)
            if not y:
                return x
            if x == y:
                continue
            else:
                heapq.heappush_max(heap,x-y)
        if len(heap) == 1:
            return heapq.heappop_max(heap)
        else:
            return 0
            
        