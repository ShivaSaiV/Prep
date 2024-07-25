class HeapSort(object):
    def sortArray(self, nums):
            n = len(nums)

            # heapify the whole array
            for i in range(n//2, -1, -1):
                self.heapify(nums, n, i)

            # replace largest element with last one
            for i in range(n - 1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]
                self.heapify(nums, i, 0)

            return nums
            
            
        
    def heapify(self, nums, n, i):
        maximum = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and nums[maximum] < nums[l]:
            maximum = l

        if r < n and nums[maximum] < nums[r]:
            maximum = r

        if maximum != i:
            nums[i], nums[maximum] = nums[maximum], nums[i]
            self.heapify(nums, n, maximum)
        

test = HeapSort()
print(test.sortArray([2,4,5,6,3,2]))

import heapq
class HeapSort2(object):
    def heapSort(self, nums):
        heapq.heapify(nums)

        n = len(nums)

        newList = [0] * n

        for i in range(n):
            minn = heapq.heappop(nums)
            newList[i] = minn

        return newList
    
test2 = HeapSort2()
print(test2.heapSort([2,4,5,6,3,2]))
