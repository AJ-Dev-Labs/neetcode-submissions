class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [-1]*2
        indexMap = {}

        for i, item in enumerate(nums):
            diff = target-item
            if diff in indexMap.keys():
                res[0] = i
                res[1] = (indexMap.get(diff))
                break
            else:
                indexMap[item]  = i
        return sorted(res)

        