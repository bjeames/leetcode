class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []
        self.is_empty = True
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.is_empty == True:
            self.is_empty = False
        
    def pop(self) -> int:
        while self.stack:
            self.temp.append(self.stack.pop())
        val = self.temp.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        if len(self.stack) == 0:
            self.is_empty = True
        return val
    
    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:
        return self.is_empty
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()