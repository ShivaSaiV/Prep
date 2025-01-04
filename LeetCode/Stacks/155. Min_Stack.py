# https://leetcode.com/problems/min-stack/description/
# Difficulty: medium 

class MinStack(object):

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val):
        self.stk.append(val)
        if len(self.min_stk) == 0:
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self):
        self.stk.pop()
        self.min_stk.pop()
        

    def top(self):
        return self.stk[-1]
        

    def getMin(self):
        return self.min_stk[-1]

test = MinStack()
test.push(3)
test.push(5)
test.pop()
print(test)
        
