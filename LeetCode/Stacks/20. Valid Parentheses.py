# https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        stk = []
        count = 0
        for i in s:
            if i == "(":
                stk.append(")")
                count += 1
            elif i == "{":
                stk.append("}")
                count += 1
            elif i == "[":
                stk.append("]")
                count += 1
            else:
                count -= 1
                if stk:
                    if i == stk[-1]:
                        stk.pop() 
                    else:
                        return False
        if count < 0:
            return False
        if len(stk) == 0: 
            return True
        return False

test = Solution()
print(test.isValid("{[]}"))