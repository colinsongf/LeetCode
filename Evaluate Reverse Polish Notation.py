class Solution:
    def evalRPN(self, tokens):
        stack=[]
        for token in tokens:
            if token in '+-*/':
                num1=stack.pop()
                num2=stack.pop()
                if token=='+':
                    stack.append(num1+num2)
                elif token=='-':
                    stack.append(num2-num1)
                elif token=='*':
                    stack.append(num1*num2)
                else:
                    result = abs(num2)/abs(num1)
                    if num2*num1 < 0:
                        result = -result
                    stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
