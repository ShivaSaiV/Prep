class Solution(object):
    def maxDistance(self, position, m):
        if m == 2:
            return max(position) - min(position)
        position.sort()

        start = 0
        n = len(position)
        end = max(position)

        while (start <= end):
            mid = start + (end - start ) // 2

            doIt = False

            count = 1
            first = position[0]
            for i in range(1, n):
                if position[i] - first >= mid:
                    count += 1
                    first = position[i]
                if count >= m:
                    doIt = True

            print(doIt)

            if doIt == True:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans

            

        


test = Solution()
print(test.maxDistance([5,4,3,2,1,1000000000], 2))

print(test.maxDistance([1,2,3,4,7], 3))

print(test.maxDistance([79,74,57,22], 4))
