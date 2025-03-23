# https://leetcode.com/problems/find-if-path-exists-in-graph/
# Difficulty: Easy

'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
'''
from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        if n == 0:
            return False
        if not edges:
            return False
        
        # create a adjacency list
        D = defaultdict(list)
        for u, v in edges:
            D[u].append(v)
            D[v].append(u)

        seen = set()
        seen.add(source)
        nodes = []
        def dfs(node):
            nodes.append(node)
            for neighbor in D[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        dfs(source)
        if destination in seen:
            return True
        else:
            return False
        
                


        
