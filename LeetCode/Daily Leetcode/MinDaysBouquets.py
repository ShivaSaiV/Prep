class Solution(object):
    def minDays(self, bloomDay, m, k):
        minDays = min(bloomDay)
        maxDays = max(bloomDay)
        numFlowers = k * m 
        if numFlowers > len(bloomDay):
            return -1
        
        while (minDays < maxDays):
            mid = (minDays + maxDays) // 2
            if self.works(bloomDay=bloomDay, m=m, k=k, d=mid):
                maxDays = mid
            
            else:
                minDays = mid + 1

        return minDays
    
    def works(self, bloomDay, m, k, d):
        total = 0
        count = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= d:
                count += 1
                if count == k:
                    total += 1
                    count = 0
            else:
                count = 0
            if total >= m:
                return True

        return False

test = Solution()
print(test.minDays([1,10,3,10,2], 3, 2))
print(test.minDays([7,7,7,7,12,7,7], 2, 3))