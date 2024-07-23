class Solution(object):
    def sortPeople(self, names, heights):
        myDict = {}
        for h in heights:
            for n in names:
                myDict[h] = n
                names.remove(n)
                break
        
        newHeights = sorted(heights, reverse= True)
        newNames = [myDict[height] for height in newHeights]
        

        return newNames

test = Solution()
print(test.sortPeople(["Mary","John","Emma"], [180, 165, 170]))