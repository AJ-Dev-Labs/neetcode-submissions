class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i  in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visting = set()

        def dfs(course):
            if course in visting:
                return False
            
            if graph[course] == []:
                return True

            visting.add(course)

            for req in graph[course]:
                if not dfs(req):
                    return False
            
            visting.remove(course)

            graph[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        
        