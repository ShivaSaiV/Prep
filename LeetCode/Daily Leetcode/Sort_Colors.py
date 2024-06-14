class Solution(object):
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for k in range(low, high):
            if arr[k] <= pivot:
                i = i + 1
                temp = arr[i]
                arr[i] = arr[k]
                arr[k] = temp
        
        temp1 = arr[i + 1]
        arr[i + 1] = arr[high]
        arr[high] = temp1

        return i + 1
    
    def quicksort(self, arr, low, high):
        if low < high:
            par = self.partition(arr, low, high)
            self.quicksort(arr, low, par - 1)
            self.quicksort(arr, par + 1, high)

        return arr
    
    def sortColors(self, nums):
        nums =  self.quicksort(nums, 0, len(nums) - 1)
        return nums

    

test = Solution()
print(test.sortColors([2,0,2,1,1,0]))