class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        for i in nums:
            if i in temp:
                return True
            else:
                temp.append(i)
        return False
        