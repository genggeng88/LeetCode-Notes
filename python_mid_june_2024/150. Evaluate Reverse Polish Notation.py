class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        arith = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in arith:
                stack.append(int(token))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == '+':
                    stack.append(op1+op2)
                elif token == '-':
                    stack.append(op2-op1)
                elif token == '*':
                    stack.append(op1*op2)
                else:
                    stack.append(int(op2/op1))
        
        return stack.pop()