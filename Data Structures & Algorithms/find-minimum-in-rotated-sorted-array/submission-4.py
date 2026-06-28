class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        low = 0
        high = len(nums) - 1

        while low <= high:
            if nums[low] < nums[high]:
                mini = min(mini, nums[low])
                break

            mid = (low + high) // 2
            mini = min(mini, nums[mid])

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return mini
        
        