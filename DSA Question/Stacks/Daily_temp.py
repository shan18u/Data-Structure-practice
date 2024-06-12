class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # our results and no. of warmer days will be stored here ;)
        stack = []  

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # check if stack is emprt AND check if this t is greater than the top of our stack 
                stackT, stackInd = stack.pop() # pop both temp and index from the stack
                res[stackInd] = i - stackInd # use that index to compute the no. of days, means currindex - index from stack. Check doc 
            stack.append((t, i)) # add the pair in the stack
        return res
