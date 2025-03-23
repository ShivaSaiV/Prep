# https://leetcode.com/problems/clone-graph/description/
# Difficulty: Medium

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return None
        
        start = node
        stack = [start]
        o_to_n = {}
        seen = set()
        seen.add(start)

        while stack:
            node = stack.pop()
            o_to_n[node] = Node(val = node.val)

            for neighbor in node.neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        
        for old_node, new_node in o_to_n.items():
            for neighbor in old_node.neighbors:
                new_neighbor = o_to_n[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return o_to_n[start]
        