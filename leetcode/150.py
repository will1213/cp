class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        add = lambda a,b : a+b
        minus = lambda a,b : a-b
        mult = lambda a,b : a*b
        div = lambda a,b : int(a/b)
        events = {
            "+": add,
            "-": minus,
            "/": div,
            "*": mult,
        }
        expression = ['+', '-', '*', '/']
        
        stack = []
        for token in tokens:
            if token in expression:
                b = stack.pop()
                a = stack.pop()
                stack.append(events[token](a,b))
            else:
                stack.append(int(token))
        return stack[-1]