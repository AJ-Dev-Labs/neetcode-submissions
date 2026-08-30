class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i  in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        total = 0

        while queue:
            course = queue.popleft()
            total += 1

            for req in graph[course]:
                indegree[req] -= 1

                if indegree[req] == 0:
                    queue.append(req)
        
        return total == numCourses

        
        