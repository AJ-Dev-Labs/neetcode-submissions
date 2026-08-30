class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i+1]

            minLength = min(len(a), len(b))
            if len(a) > len(b) and a[:minLength] == b[:minLength]:
                return ""
            
            for j in range(minLength):
                if a[j] != b[j]:
                    adj[a[j]].add(b[j])
                    break
        
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
