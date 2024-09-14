# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty: Medium

class Solution(object):
    def evalRPN(self, tokens):
        stk1 = []
        for i in tokens:
            if i != "+" and i != "-" and i != "*" and i != "/":
                stk1.append(int(i))
            if i == "+":
                x = stk1.pop()
                y = stk1.pop()
                stk1.append(x + y)
            if i == "*":
                x = stk1.pop()
                y = stk1.pop()
                stk1.append(x * y)
            if i == "-":
                x = stk1.pop()
                y = stk1.pop()
                stk1.append(y - x)
            if i == "/":
                x = stk1.pop()
                y = stk1.pop()
                stk1.append(int(float(y) / x))
            
        return stk1[0]

test = Solution()
# print(test.evalRPN(["2","1","+","3","*"]))
# print(test.evalRPN(["4","13","5","/","+"]))
# print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))