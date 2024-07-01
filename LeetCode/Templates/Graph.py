class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
            print(self.graph_dict)

    def getPaths(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        
        for node in self.graph_dict[start]:
            if node not in path:
                newPath = self.getPaths(node, end, path)
                
                for p in newPath:
                    paths.append(p)

        return paths
    
    def getShortestPath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        print(self.graph_dict)

        if start not in self.graph_dict:
            return None
        
        shortest = None
        
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.getShortestPath(node, end, path)
                
                if sp:
                    if shortest is None:
                        shortest = sp

                    if len(sp) < len(shortest):
                        shortest = sp

        return shortest

                    

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Paris", "Dubai"),
        ("Mumbai", "Dubai"),
        ("Paris", "New York")
    ]

    routeGraph = Graph(routes)

    start = "Mumbai"
    end = "Paris"

    print(routeGraph.getPaths(start, end))
    print(routeGraph.getShortestPath(start, end))
    

    # Finding Degree (2d Array)

class Solution(object):
        def findCenter(self, edges):
            visited = []
            count = 0
            
            for i in range(len(edges)):
                if edges[i][0] not in visited:
                    count += 1
                    visited.append(edges[i][0])

                if edges[i][1] not in visited:
                    count += 1
                    visited.append(edges[i][1])

            print(count)
            degree = [0 for i in range(count + 1)]


            for i in range(len(edges)):
                degree[edges[i][0]] += 1
                degree[edges[i][1]] += 1

            return degree
            


test = Solution()
print(test.findCenter([[1,2],[2,3],[4,2]]))
