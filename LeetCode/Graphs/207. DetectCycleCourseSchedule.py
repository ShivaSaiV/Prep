# https://leetcode.com/problems/course-schedule/description/
# Difficulty: Medium

'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        D = defaultdict(list)
        
        for a, b in prerequisites:
            D[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

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
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        


# Kahn's Algorithm - Queue
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        D = defaultdict(list)
        
        for a, b in prerequisites:
            D[a].append(b)

        # Calculate number of prerequisites for each course
        indegree = [0] * numCourses
        for nodes in D.values():
            for j in nodes:
                indegree[j] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            node = q.popleft()
            count += 1

            for i in D[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        return count == numCourses
        