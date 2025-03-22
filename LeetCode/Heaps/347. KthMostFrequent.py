# https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium

'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        # Counting frequencies - O(n)
        myDict = {}
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        print(myDict)
        heap = []

        # Build the heap
        for key, v in myDict.items():
            if len(heap) < k:
                heapq.heappush(heap, (v, key))
            else:
                heapq.heappushpop(heap, (v, key))
        
        print(heap)

        res = []
        for i in heap:
            res.append(i[1])

        return res

test = Solution()
print(test.topKFrequent([1,1,1,2,2,3], 2))

# Buckets
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n + 1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        
        return ret

# Time Complexity: O(n)
# Space Complexity: O(n)
        
        