# https://leetcode.com/problems/k-closest-points-to-origin/
# Difficulty: Medium

'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

'''
Steps: k log n
- Find distance from origin for each point
- Build min or max heap 
- Pop out k closest points
'''
import math
import heapq

# Max Heap - better
class Solution(object):
    def kClosest(self, points, k):
        def dist(x, y):
            return x**2 + y**2
        
        heap = []
        for x, y in points:
            d = dist(x, y)
            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            else:
                heapq.heappushpop(heap, (-d, x, y))

        res = []

        print(heap)
        
        for d, x, y in heap:
            res.append(list([x, y]))

        return res

# Heapify
class Solution3(object):
    def kClosest(self, points, k):
        distanceArr = []
        for x, y in points:
            distanceArr.append((x**2 + y**2, x, y))
        
        heapq.heapify(distanceArr)
        res = []

        for i in range(k):
            d, x, y = heapq.heappop(distanceArr)
            res.append(list([x, y]))
        print(distanceArr)
        return res


# Min heap
class Solution2(object):
    def kClosest(self, points, k):
        # Calculate distances from origin for each point
        distanceDict = {}
        for i in points:
            temp = tuple(i)
            distanceDict[temp] = math.sqrt(i[0]**2 + i[1]**2)

        heap = []
        for key, val in distanceDict.items():
            heapq.heappush(heap, (val, key))

        res = []

        for i in range(k):
            res.append(list(heapq.heappop(heap)[1]))

        return res        

test = Solution3()
print(test.kClosest([[1, 3], [-2, 2]], 1))
print(test.kClosest([[3,3],[5,-1],[-2,4]], 2))


        