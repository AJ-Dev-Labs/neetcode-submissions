class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for next_node in graph[node]:
                dfs(next_node)

        dfs(0)
        return len(visited) == n
        