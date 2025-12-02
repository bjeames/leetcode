class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and ast < 0:
                top = stack[-1]
                if abs(top) > abs(ast):
                    alive=False
                elif abs(top) < abs(ast):
                    stack.pop()
                elif abs(top) == abs(ast):
                    stack.pop()
                    alive=False
            if alive:
                stack.append(ast)
        return stack

        

