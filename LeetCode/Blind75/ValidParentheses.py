class Solution:
    def isValid(self, s):

        stack = []
        n = len(s)
        count = 0

        for i in range(n):
            if s[i] == "[":
                stack.append("]")
                count += 1
            elif s[i] == "{":
                stack.append("}")
                count += 1
            elif s[i] == "(":
                stack.append(")")
                count += 1
            else:
                count -= 1
                if stack:
                    if s[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False

        if count < 0:
            return False
        
        if len(stack) == 0:
            return True
        else:
            return False

test = Solution()
print(test.isValid("[(])"))