class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, i in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx+1, len(nums) - 1
            while left < right:
                threesum = i + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([i, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res