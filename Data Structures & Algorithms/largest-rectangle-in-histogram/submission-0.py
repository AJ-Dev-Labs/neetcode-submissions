class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxA = 0
        stack = []

        for idx, h in enumerate(heights):
            startIdx = idx
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxA = max(maxA, height * (idx - index))
                startIdx = index
            stack.append((startIdx, h))
        
        for i, h in stack:
            maxA = max(maxA, h * (len(heights) - i))
        return maxA
        