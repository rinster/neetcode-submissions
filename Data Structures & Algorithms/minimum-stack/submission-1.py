class MinStack:
    # Space O(1)
    def __init__(self):
        self.stack = []
        self.min_val = float('-inf')
        
    def push(self, value: int) -> None:
        if not self.stack: # perfect case, empty stack 
            self.stack.append(value)
            self.min_val = value
        elif value >= self.min_val: # case new val is greater than min
            # normal case: val doesn't set a new min, just store it as-is
            self.stack.append(value)
        else:
            # val is the new min — encode it so we can recover the OLD min on pop
            # encoded = 2*val - old_min  (equivalent to your "min - 2*diff" idea)
            self.stack.append(2 * value - self.min_val)
            self.min_val = value  # update current min


    def pop(self) -> None:
        top = self.stack.pop()
        if top < self.min_val:
            # this was an encoded value — it means it USED to be the min
            # so popping it means we need to restore the previous min
            old_min = self.min_val
            self.min_val = 2 * old_min - top  # decode to get the min before this push
        # if top >= self.min_val, it was a normal value, min_val stays the same
        

    def top(self) -> int:
        if self.stack[-1] < self.min_val:
            # encoded — the "real" top value is actually the current min
            return self.min_val
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_val
        