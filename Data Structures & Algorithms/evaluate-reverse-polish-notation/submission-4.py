class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def performOp(num1, num2, op):
            num1 = int(num1)
            num2 = int(num2)
            if op == "+":
                return num1 + num2
            elif op == "-":
                return num1 - num2
            elif op == "*":
                return num1 * num2
            else: 
                return int(num1 / num2)
        
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ["+", "/", "*", "-"]:
                num2 = stack.pop()
                num1 = stack.pop()
                res = performOp(num1, num2, tokens[i]) 
                stack.append(res)
            else:
                stack.append(tokens[i])
        return int(stack[-1])


            
        
            