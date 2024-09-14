# https://leetcode.com/problems/baseball-game/
# Difficulty: easy

class Solution(object):
    def calPoints(self, operations):
        resArr = []
        for i in range(len(operations)):
            if operations[i] != "+" and operations[i] != "D" and operations[i] != "C":
                resArr.append(int(operations[i]))
            if operations[i] == "+":
                num1 = resArr.pop()
                num2 = resArr.pop()
                resArr.append(num2)
                resArr.append(num1)
                resArr.append(num1 + num2)
            if operations[i] == "D":
                num1 = resArr.pop()
                resArr.append(num1)
                resArr.append(2 * num1)
            if operations[i] == "C":
                resArr.pop()

            print(resArr)
            

        res = 0
        for i in resArr:
            res += i
                

        return res


test = Solution()
# print(test.calPoints(["5","2","C","D","+"]))
print(test.calPoints(["5","-2","4","C","D","9","+","+"]))