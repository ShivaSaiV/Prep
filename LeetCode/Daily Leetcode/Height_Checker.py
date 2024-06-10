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
        sorted_arr = arr
        if low < high:
            par = self.partition(sorted_arr, low, high)
            self.quicksort(sorted_arr, low, par - 1)
            self.quicksort(sorted_arr, par + 1, high)

        return sorted_arr
    
    def heightChecker(self, heights):
        n = len(heights) - 1
        unordered = []
        for i in range(n + 1):
            unordered.append(heights[i])
        print(unordered)
        sorted_heights = self.quicksort(heights, 0, n)

        count = 0
        print(unordered)
        for i in range(n + 1):
            if sorted_heights[i] != unordered[i]:
                count += 1

        return count
    
    
ans = Solution()
print(ans.heightChecker([1,1,4,2,1,3]))