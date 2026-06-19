class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        maxS = 0

        for i in numSet:
            if not i-1 in numSet:
                countS = 1
                j=i 
                while(j+1 in numSet):
                    countS += 1
                    j = j+1
                maxS = max(countS, maxS)
        return maxS

        