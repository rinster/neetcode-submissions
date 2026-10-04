class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
        # Why this works
            # The sign of the stored number is the key:

            # diff >= 0 → no new min was set on this push.
            # diff < 0 → a new min was set, and self.min currently holds that value.
            # This is why pop() can restore the previous minimum, but only when it encounters a negative diff — that's the whole point of the encoding.
    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop
        
    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
