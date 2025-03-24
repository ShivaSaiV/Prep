# Bucket Sort Solution
class Solution():
    def topKFrequent(self, nums, k):
        count = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            frequencies[c].append(n)

        res = []
        for i in range(len(frequencies) - 1, 0, -1):
            for n in frequencies[i]:
                res.append(n)
                if len(res) == k:
                    return res 


# Heap Solution
class Solution():
    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []

        for key, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        res = []
        for i in heap:
            res.append(i[1])
        
        return res
    
        
        