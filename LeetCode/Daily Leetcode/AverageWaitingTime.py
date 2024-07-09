class Solution(object):
    def averageWaitingTime(self, customers):
        totalWait = 0
        numCustomers = len(customers)
        finish = customers[0][0]
        for i in customers:
            print("I[0]" + str(i[0]))
            if i[0] <= finish:
                finish += i[1]
                wait = finish - i[0]
                totalWait += wait
                print("Finish: " + str(finish))
                print("Wait: " + str(wait))
            else:
                print("Hello")
                finish = i[0] + i[1]
                wait = finish - i[0]
                totalWait += wait
                print("Finish: " + str(finish))
                print("Wait: " + str(wait))


            print(totalWait)
        return float(totalWait) / numCustomers

test = Solution()
print(test.averageWaitingTime([[1,2],[2,5],[4,3]]))
print(test.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
