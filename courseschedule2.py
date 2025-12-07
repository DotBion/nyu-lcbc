from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        in_degree = [0]*numCourses
        graph = defaultdict(list)
        for course, pre_req in prerequisites:
            graph[pre_req].append(course)
            in_degree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        while queue:
            curr_course = queue.popleft()
            ans.append(curr_course)
            for neigh in graph[curr_course]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
        return ans if len(ans) == numCourses else []




        
