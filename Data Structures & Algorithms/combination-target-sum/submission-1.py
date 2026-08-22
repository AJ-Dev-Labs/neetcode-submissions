class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #version 2 with sorted array
        nums.sort()
        res = []

        def dfs(i, cur, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                n = nums[j]

                if n > remaining:
                    break;

                cur.append(n)
                dfs(j, cur, remaining - n)
                cur.pop()
        
        dfs(0, [], target)
        return res
        