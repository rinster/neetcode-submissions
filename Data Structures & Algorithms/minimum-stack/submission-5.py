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
            if val < self.min: # new min if number is negative
                self.min = val
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

# The core idea: the stack stores distance from the current min, not the value. A negative number means “this push became the new min, and the size of the drop tells me what the old min was.” That’s how O(1) space per element works with no second stack.

# Memory technique: a mountain climber’s altitude log.

# Min = the lowest point reached so far (the camp).
# Each push logs how far above or below camp you are.
# Negative entry = you went below camp, so you move camp lower, and the entry remembers the old camp.
# Walking back (pop) over a negative entry means you climb out of the pit, so camp jumps back to where it was: min - diff.

