class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Get an empty Stack, where you will push strings in
        stack = []

        # get a loop, that will allow you to run iteration to the entire list and will add integers to our empty stack 
        for c in tokens:
            # if we get only number we go to else statement, which will perform the operation based on the operator.  
            # like [2, 3] -> "+" -> run 2 pops -> [2] -> [], -> add both 2+3= 5 -> push back to the stack -> [5]

            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # we will have to assign the values to variables here bcz 
                # you dont wanna do 2-3, thats wrong instead do 3-2, which is first pop last element and so on
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            # why we use float(b) / a instead of b // a bcz 
            # if we use // it would not allow us to use int that we need to round down
            # we need float cuz this will allow us to handle cases where the result is not an integer
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a)) 
            else:
                stack.append(int(c))
        return stack[0]
