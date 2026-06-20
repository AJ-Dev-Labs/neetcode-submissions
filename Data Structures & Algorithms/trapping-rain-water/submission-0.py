class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[-1]

        l = 0
        r = len(height) - 1
        water = 0
        while l < r:
            if maxL <= maxR:
                h = maxL - height[l]
                if h > 0:
                    water = water + h
                maxL = max(maxL, height[l])
            else:
                h = maxR - height[r]
                if h > 0:
                    water = water + h
                maxR = max(maxR, height[r])
            if maxL <= maxR:
                l += 1
            else:
                r -= 1
        return water

        