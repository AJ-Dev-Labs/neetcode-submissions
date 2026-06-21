class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "+":
                b = stack.pop()
                a = stack.pop()
                res = a + b
                stack.append(res)
            elif s == "-":
                b = stack.pop()
                a = stack.pop()
                res = a - b
                stack.append(res)
            elif s == "*":
                b = stack.pop()
                a = stack.pop()
                res = a * b
                stack.append(res)
            elif s == "/":
                b = stack.pop()
                a = stack.pop()
                res = int(a / b)
                stack.append(res)
            else:
                stack.append(int(s))
        return stack.pop()
        