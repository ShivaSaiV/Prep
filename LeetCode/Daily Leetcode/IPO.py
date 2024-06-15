import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        projs = [0] * len(capital)

        for i in range(len(capital)):
            proj = (capital[i], profits[i])
            projs[i] = proj
            
        projs.sort()
        

        profAv = []

        for i in range(k):
            
            while projs and projs[0][0] <= w:
                c, p = heapq.heappop(projs)                
                heapq.heappush(profAv, -1 * p)

            if not profAv:
                break

            w += -1 * heapq.heappop(profAv)


        return w
    

test = Solution()
print(test.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
print(test.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))