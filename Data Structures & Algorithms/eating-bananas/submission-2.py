class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        maxN = max(piles)
        low = 1
        high = maxN
        k = -1
        while low <= high:
            mid = (low+high)//2
            sH = 0
            for i in piles:
                hour = 1
                if i % mid == 0:
                    hour = i // mid
                else:
                    hour = (i // mid) + 1
                sH = sH + hour
            if sH <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1
        return k
            