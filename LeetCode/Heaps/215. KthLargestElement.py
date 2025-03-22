# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Difficulty: Medium

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

length - k
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



# Using Quick-Select
class Solution3(object):
    # Time: O(N) - Average
    def findKthLargest(self, nums, k):
        target_index = len(nums) - k

        # recursive quickselect algo
        def quickSelect(l, r):
            # pivot = rightmost element
            pivot = nums[r]
            ptr = l

            for i in range(l, r):
                # Partition - leftside/rightside based on val
                if nums[i] <= pivot:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            
            nums[ptr], nums[r] = nums[r], nums[ptr]
            
            # choose the leftside of the array
            if ptr > k:
                return quickSelect(l, ptr - 1)
            # choose the rightside of the array
            elif:
                return quickSelect(ptr + 1, r)
            # pivot is the ans
            else:
                return nums[p]
        
        return quickSelect(0, len(nums) - 1)








test = Solution2()
test.findKthLargest([3,2,1,5,6,4], 2)
        