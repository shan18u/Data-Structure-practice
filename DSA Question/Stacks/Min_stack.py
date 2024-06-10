class MinStack:
    def __init__(self): # we will use 2 Stacks 
        self.stack = [] # This stack will enter all the elements from the question one by one
        self.minStack = [] # this stack will only enter those elements which are smaller then all the elements that are already in the minstack. Only minimum is allowed

    def push(self, val: int) -> None:
        self.stack.append(val) # add the element into the stack
        val = min(val, self.minStack[-1] if self.minStack else val) # check if minstack is Non-empty OR if the potential element is less than the last minimum added element in the stack. Last added number is usually smallest of all. 
        self.minStack.append(val) 

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # get the last value or element is the top value

    def getMin(self) -> int:
        return self.minStack[-1] # same reasoning last one will be the smallest
