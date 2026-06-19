class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        left = 1
        right = len(numbers)

        while left < right:
            if numbers[left-1] + numbers[right - 1] > target:
                right -= 1
            elif numbers[left-1] + numbers[right - 1] < target:
                left += 1
            else:
                res.append(left)
                res.append(right)
                return res
        