class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        targetMap = {}
        windowMap = {}

        for i in t:
            targetMap[i] = 1 + targetMap.get(i, 0)
            windowMap[i] = 0
        
        mTarget = len(targetMap)
        wTarget = 0
        startIdx = 0
        endIdx = -1
        minL = float('inf')

        l = 0
        for r in range(len(s)):
            if s[r] in windowMap:
                windowMap[s[r]] += 1
                if windowMap[s[r]] == targetMap[s[r]]:
                    wTarget += 1
            
            if wTarget == mTarget:
                while wTarget == mTarget:
                    if (r - l + 1) < minL:
                        minL = r-l+1
                        startIdx = l
                        endIdx = r
                    if s[l] in windowMap:
                        if windowMap[s[l]] == targetMap[s[l]]:
                            wTarget -= 1
                        windowMap[s[l]] -= 1
                    
                    l += 1
        res = ""
        for i in range(startIdx, endIdx + 1):
            res = res + s[i]
        return res
