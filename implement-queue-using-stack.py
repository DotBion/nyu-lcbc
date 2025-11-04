class MyQueue:

    def __init__(self):
        self.stack1 = []
    def push(self, x: int) -> None:
        self.stack1.append(x)
    def pop(self) -> int:
        stack2 = []
        l = len(self.stack1)
        for i in range(l) :
            stack2.append(self.stack1.pop())
        x = stack2.pop()
        self.stack1 = stack2[::-1]
        return x
    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if self.stack1 == [] :
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
