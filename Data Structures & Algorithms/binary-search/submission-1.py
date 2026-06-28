class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        res = -1
        while l <= h:
            m = l + (h-l)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1
            else:
                res = m
                break
            
        return res
        
        