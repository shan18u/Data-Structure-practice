class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Important maybe use dfs too
        stack = []
        res = [] # our result that we will return?>>

        def backtrack(openN, closedN):
            if openN == closedN == n: 
                res.append("".join(stack))  # join that list of string into 1 list and thats our answer
                return

            # we need this condition to make sure that we don't get open any bracket if we have exceeded the n
            # only open if open is less than given number
            if openN < n: 
                stack.append("(")
                backtrack(openN + 1, closedN) # backtrack and perform
                stack.pop() # undo the append that we just did 

            # we need this condition to make sure that we don't close any bracket that has no open
            # only close if close is less than already open brackets
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1) # backtrack and perform
                stack.pop() # undo the append that we just did 

        backtrack(0, 0)
        return res
