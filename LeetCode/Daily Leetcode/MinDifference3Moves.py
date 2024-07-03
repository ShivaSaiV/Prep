class Solution(object):
    def minDifference(self, nums):
        n = len(nums)

        if n <= 4:
            return 0
        
        nums.sort()

        minDiff = 0

        remLast = nums[:n-3]
        remFirst = nums[3:n]

        print(remLast)
        print(remFirst)

        minDiff = max(remLast) - min(remLast)

        minDiff = min(minDiff, max(remFirst) - min(remFirst))

        remFirstLast2 = nums[1:n-2]
        rremFirst2Last = nums[2:n-1]

        print(remFirstLast2)
        print(rremFirst2Last)

        minDiff = min(minDiff, max(remFirstLast2) - min(remFirstLast2))

        minDiff = min(minDiff, max(rremFirst2Last) - min(rremFirst2Last))

        return minDiff




test = Solution()
print(test.minDifference([1,5,0,10,14]))
print(test.minDifference([6,6,0,1,1,4,6]))
# 0, 1, 1, 4, 6, 6, 6
# 0, 1, 5, 10, 14

print(test.minDifference([82,81,95,75,20]))
# 20, 75, 81, 82, 95
