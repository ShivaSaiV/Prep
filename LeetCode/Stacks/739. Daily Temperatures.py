# https://leetcode.com/problems/daily-temperatures/description/
# Medium

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


class Solution(object):
    def dailyTemperatures(self, temperatures):
        # start = 1
        # i = 1
        # prev = 0
        # temp = 1
        # stk = []
        # res = []
        # stk.append(temperatures[0])
        # while (i < len(temperatures) - 1):
        #     if temperatures[start] > stk[-1]:
        #         stk.pop()
        #         stk.append(temperatures[i])
        #         res.append(start - prev)
        #         prev = i
        #     else:
        #         temp -= 1
        #     i += 1
        #     start += 1
        # return res
        res = [0] * len(temperatures) 
        stk = []
        for i in range(len(temperatures)):
            while True:
                if len(stk) == 0:
                    break
                if temperatures[stk[-1]] < temperatures[i]:
                    prev = stk.pop()
                    res[prev] = i - prev
                else:
                    break
            stk.append(i)
        return res



test = Solution()
print(test.dailyTemperatures([73,74,75,71,69,72,76,73]))