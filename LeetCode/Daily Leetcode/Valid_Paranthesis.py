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