# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Difficulty: Medium

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
'''

import heapq

# Using a Max Heap
class Solution(object):
    # Time: O(N + klog N)
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)


# Using a Min Heap
class Solution2(object):
    # Time: O(N log K)
    def findKthLargest(self, nums, k):
        min_heap = []

        for i in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, i)
            else:
                heapq.heappushpop(min_heap, i)
            print(min_heap)
        return min_heap[0]



test = Solution2()
test.findKthLargest([3,2,1,5,6,4], 2)
        