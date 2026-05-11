class MinStack:

    def __init__(self):
        self.stack = []      # regular stack to store values
        self.min_stack = []  # keeps track of the min at each level

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If min_stack is empty or val <= current min, push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
