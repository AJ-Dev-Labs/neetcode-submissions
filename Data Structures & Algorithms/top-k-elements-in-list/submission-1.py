class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        for item in nums:
            if item in countMap:
                countMap[item] += 1
            else:
                countMap[item] = 1
        
        for key, val in countMap.items():
            bucket[val].append(key)
        
        for i in range(len(bucket)-1, 0, -1):
            for c in bucket[i]:
                res.append(c)
                if len(res) == k:
                    return res
        