class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        targetMap = {}
        windowMap = {}

        for i in t:
            targetMap[i] = 1 + targetMap.get(i, 0)
        
        mTarget = len(targetMap)
        wTarget = 0
        startIdx = -1
        endIdx = -1
        minL = float('inf')

        l = 0
        for r in range(len(s)):
            c = s[r]
            windowMap[c] = 1 + windowMap.get(c, 0)

            if c in targetMap and windowMap[c] == targetMap[c]:
                wTarget += 1
            
            while wTarget == mTarget:
                if (r - l + 1) < minL:
                    minL = r-l+1
                    startIdx = l
                    endIdx = r
                windowMap[s[l]] -= 1
                if s[l] in targetMap and windowMap[s[l]] < targetMap[s[l]]:
                    wTarget -= 1
                l += 1
        return s[startIdx: endIdx + 1] if minL != float('inf') else ""
