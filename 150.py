class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                first = stack.pop()
                sec = stack.pop()
                if token == '+':
                    stack.append(sec + first)
                elif token == '-':
                    stack.append(sec - first)
                elif token == '*':
                    stack.append(sec * first)
                else:
                    stack.append(int(sec/first))

        return round(stack.pop())