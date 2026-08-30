class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = [False] * n
        component = 0

        def dfs(node):
            visited[node] = True

            for next_node in graph[node]:
                if not visited[next_node]:
                    dfs(next_node)
        
        for i in range(n):
            if not visited[i]:
                component += 1
                dfs(i)
        
        return component
        