class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(")")
            elif s[i] == "[":
                stack.append("]")
            elif s[i] == "{":
                stack.append("}")
            elif (len(stack) == 0 or (stack.pop() != s[i])):
                return False

        if len(stack) == 0:
            return True
    def check_parentheses_balance(self, input_string):
        stack = []

        for char in input_string:
            if char == "(":
                stack.append(char)
            elif char == ")" and stack:
                stack.pop()
            else:
                print("unbalanced")
                return
        print("balanced")

    def addFun(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 2
        return self.addFun(n - 1) + self.addFun(n - 2)

test = Solution()
print(test.addFun(6))