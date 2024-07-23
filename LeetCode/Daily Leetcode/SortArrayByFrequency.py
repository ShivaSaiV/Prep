class Solution(object):
    def frequencySort(self, nums):
        myDict = {}
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

        print(myDict)

        res = []

        newTup = (sorted(myDict.items(), key = lambda x: x[0], reverse = True))
        newTup = (sorted(newTup, key = lambda x: x[1]))
        print(newTup)
        for key, value in newTup:
            res.extend([key] * value)

        return res

        


test = Solution()
# print(test.frequencySort([1,1,2,2,2,3]))
# print(test.frequencySort([2,3,1,3,2]))
print(test.frequencySort([-1,1,-6,4,5,-6,1,4,1]))