class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for c1, c2 in prerequisites:
            graph[c1].append(c2)

        curr = set()

        def dfs(course) -> bool:
            if course in curr:
                return False
            curr.add(course)
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            curr.remove(course) 
            return True

        # go through every course because of disjoint
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True