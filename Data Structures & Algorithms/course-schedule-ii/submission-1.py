class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i: [] for i in range(numCourses)}
        path = set()
        visited = set()
        schedule = []

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            for crs in graph[course]:
                if not dfs(crs):
                    return False
            
            path.remove(course)
            visited.add(course)
            schedule.append(course)
            return True


        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return schedule

