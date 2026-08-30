class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = [False] * n

        def dfs(node):
            if visited[node]:
                return

            visited[node] = True

            for next_node in graph[node]:
                dfs(next_node)

        dfs(0)
        return all(visited)
        