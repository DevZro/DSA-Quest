# Min Stack

class MinStack:

    def __init__(self):
        self.data = []
        self.min_index = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min_index or val < self.data[self.min_index[-1]]:
            self.min_index.append(len(self.data) - 1)

    def pop(self) -> None:
        self.data.pop()
        if len(self.data) == self.min_index[-1]:
            self.min_index.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.data[self.min_index[-1]]