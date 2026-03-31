class MinStack:

    def __init__(self):
        stack = []
        self.stack = stack

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        stackMin = float("infinity")
        for i in range(len(self.stack)):
            if self.stack[i] < stackMin:
                stackMin = self.stack[i]
        return stackMin

        #return min(self.stack)


    