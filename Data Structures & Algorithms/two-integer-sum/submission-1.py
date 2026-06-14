class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i, item in enumerate(nums):
            diff = target-item
            if diff in indexMap:
                return [indexMap[diff], i]
            else:
                indexMap[item]  = i

        