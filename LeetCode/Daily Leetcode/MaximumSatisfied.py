class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)

        windowPow = 0
        maxPow = 0
        minSatisfied = 0
        

        start = 0

        if n == 1 and minutes == 1:
            return customers[0]

        for i in range(n):
            if grumpy[i] == 0:
                minSatisfied += customers[i]

        
        for i in range(n):
            # if grumpy[i] == 1:
            windowPow += customers[i] * grumpy[i]

            if ((i - start + 1) == minutes):
                maxPow = max(maxPow, windowPow)
                windowPow -= customers[start] * grumpy[start]
                start += 1
            # if grumpy[i] == 1:
            #     windowPow -= customers[i]
            #     maxPow -= customers[i]

        return maxPow + minSatisfied 

        