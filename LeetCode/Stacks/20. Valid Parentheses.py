# https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stk = []
        for i in s:
            if i == "(":
                stk.append("(")
            elif i == "[":
                stk.append("[")
            elif i == "{":
                stk.append("{")
            elif i == ")":
                if stk:
                    if stk[-1] == "(":
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            elif i == "]":
                if stk:
                    if stk[-1] == "[":
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            elif i == "}":
                if stk:
                    if stk[-1] == "{":
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            else:
                return False
        
        if len(stk) == 0:
            return True
        else:
            return False

test = Solution()
print(test.isValid("]"))