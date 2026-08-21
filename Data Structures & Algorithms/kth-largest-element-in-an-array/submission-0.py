class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        val = 0
        for i in range(k):
            val = heapq.heappop_max(heap)
        return val
        