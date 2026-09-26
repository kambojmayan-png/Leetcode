class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for i in tokens:
            if i == '+':
                self.stack.append(self.stack.pop() + self.stack.pop())
            elif i == '-':
                a, b = self.stack.pop(),self.stack.pop()
                self.stack.append(b - a)
            elif i == '*':
                self.stack.append(self.stack.pop() * self.stack.pop())
            elif i == '/':
                a, b = self.stack.pop(),self.stack.pop()
                self.stack.append(int(b / a))
            else:
                self.stack.append(int(i))
            
        return self.stack[-1]