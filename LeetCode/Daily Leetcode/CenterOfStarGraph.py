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

        degrees = {}

        for i in range(len(edges)):
            degree[edges[i][0]] += 1
            degree[edges[i][1]] += 1

        print(degree)


        for i in range(len(edges)):
            degrees[edges[i][0]] = degree[i+1]
            degrees[edges[i][1]] = degree[i]

        print(degrees)

        # highestJ = 0
        # highestI = 0

        # for i, j in enumerate(degree):
        #     if j > highestJ:
        #         highestJ = j
        #         highestI = i

        maxVal = max(degrees.values())

        res = 0

        for key, value in degrees.items():
            if value == maxVal:
                res = key

        print(maxVal)



        return res

        


test = Solution()
print(test.findCenter([[1,2],[2,3],[4,2]]))
