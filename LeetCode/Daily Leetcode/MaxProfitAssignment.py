class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        maxProfit = 0
        n = len(difficulty)

        for i in range(n):
            for j in range(len(worker)):
                cap = worker[j]

                if difficulty[i] == cap:
                    maxProfit += profit[i]
                    
