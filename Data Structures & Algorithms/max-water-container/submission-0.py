class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        maxW = 0

        while l < r:
            h = min(heights[l], heights[r])
            maxW = max(maxW, h * (r-l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxW



        