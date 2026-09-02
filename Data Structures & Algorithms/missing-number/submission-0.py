class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        sumN = (n * (n+1)) // 2
        sumN2 = 0
        for i in nums:
            sumN2 += i
        return sumN - sumN2

        