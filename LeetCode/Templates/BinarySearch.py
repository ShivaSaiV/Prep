class BinarySearch:

    # Traditional Binary Search
    def binSearch1(self, arr, target):
        n = len(arr)
        l = 0
        r = n - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if arr[m] == target:
                return True 

            if arr[m] > target:
                r = m - 1
            
            if arr[m] < target:
                l = m + 1
        
        return False

    # Condition-based Binary Search
    def binSearch2(self, arr):
        n = len(arr)
        l = 0
        r = n - 1
        
        while l < r:
            m = l + ((r - l) // 2)

            if arr[m]:
                r = m 
            else:
                l = m + 1
        
        return l

            
test = BinarySearch()
print(test.binSearch1([1, 2, 3], -1))
print(test.binSearch2([False, False, False, True, True]))