class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            mini = min(mini, nums[mid])

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
        
        