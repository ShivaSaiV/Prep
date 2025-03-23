# https://leetcode.com/problems/course-schedule-ii/description/
# Difficulty: Medium

# DFS topological sort
from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        D = defaultdict(list)
        
        for a, b in prerequisites:
            D[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        order = []

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            
            elif state == VISITING:
                return False
            
            states[node] = VISITING

            for neighbor in D[node]:
                if not dfs(neighbor):
                    return False
            
            states[node] = VISITED
            order.append(node)
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order



# BFS
class Solution:
    def findOrder(self, numCourses, prerequisites):
        inDegree = [0] * numCourses
        adj = defaultdict(list)
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        for nodes in adj.values():
            for node in nodes:
                inDegree[node] += 1
        
        q = deque([i for i in range(numCourses) if inDegree[i] == 0])
        ans = []
        
        while q:
            node = q.popleft()
            ans.append(node)
            for ngbr in adj[node]:
                inDegree[ngbr] -= 1
                if inDegree[ngbr] == 0:
                    q.append(ngbr)
        
        ans.reverse()
        return ans if len(ans) == numCourses else []