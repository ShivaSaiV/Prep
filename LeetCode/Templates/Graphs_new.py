'''
Adjacency List: 
- Key = node's value
- Value = neighbors

Have a seen set to store already seen nodes in DFS

Time: DFS/BFS: O(V + E)
Space: O(V + E)

Trees = connected, acyclic graphs (no loop / 2 connections)

E must be N (or V) - 1, so if N = 4, E = 3 if connected and acyclic
'''

# Array of Edges (Directed)
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]


# Convert Arry of Edges -> Adjacency Matrix
M = []
for i in range(n):
    M.append([0] * n)

for u, v in A:
    M[u][v] = 1

    # If undirected
    # M[v][u] = 1


# Convert Arry of Edges -> Adjacency List
from collections import defaultdict
D = defaultdict(list)

for u, v in A:
    D[u].append(v)

    # If undirected
    # D[v].append(u)
print(D)


# DFS with Recursion - O(V + E)
def dfs_recursive(node):
    print(node)
    for neighbor in D[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            dfs_recursive(neighbor)

source = 0
seen = set()
seen.add(source)



# DFS with Iteratation Stack - O(V + E)

source = 0
seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for neighbor in D[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            stack.append(neighbor)



# BFS with Queue - O(V + E)
from collections import deque
source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for neighbor in D[node]:
        seen.add(neighbor)
        q.append(neighbor)




