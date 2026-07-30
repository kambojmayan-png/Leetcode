class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if(i in "({["):
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if( i == ')' and top == '(' or i == ']' and top == '[' or i == '}' and top == '{'):
                    stack.pop()
                else:
                    return False
        return not stack