class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])

        def rob(start, end):
            prev = nums[start]
            curr = max(nums[start], nums[start+1])

            for i in range(start+2, end):
                temp = prev
                prev = curr
                curr = max(nums[i] + temp, curr)
            return curr
        
        return max(rob(0, n-1), rob(1, n))

        
        
        