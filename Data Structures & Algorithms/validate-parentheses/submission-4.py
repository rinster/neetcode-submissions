class Solution:
    def isValid(self, s: str) -> bool:
        validP = {
            '[' : ']',
            '{' : '}',
            '(' : ')',
        }
        stack = []
        
        for char in s:
            # if opening bracket in validP
                # append to stack it's closing bracket
            # if closing bracket and there is something on stack
                #compare the stack pop to current char, if not equal return false, true, do nothing
            if char in validP:
                stack.append(validP[char])
            elif not stack:
                    return False
            else:
                if stack.pop() != char:
                    return False
            

        print(stack)
        return len(stack) == 0

# c
# ( [ { } ] )

# s = 

        