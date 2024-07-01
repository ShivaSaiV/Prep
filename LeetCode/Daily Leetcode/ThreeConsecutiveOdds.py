class Solution(object):
    def threeConsecutiveOdds(self, arr):
        first = 0
        count = 0

        while (first + 2 < len(arr)):
            second = first + 1
            third = first + 2

            print(arr[first])

            if (arr[first] % 2 == 1) and (arr[second] % 2 == 1) and (arr[third] % 2 == 1):
                return True

            first += 1
            

        return False
        

test = Solution()
print(test.threeConsecutiveOdds([2, 6, 4, 1]))
print(test.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
print(test.threeConsecutiveOdds([1, 2, 3]))


            
        