class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [] # init stack
        curr = root # pointer that will tell us what node we are at

        while stack or curr: # if curr not null and stack not empty
            while curr: 
                stack.append(curr) # add curr to stack  
                curr = curr.left # go to every node on left before we visit curr
            curr = stack.pop() # now that after loop is over our curr is at null, exit and then pop the recent val tp stack
            k -= 1 


            
            if k == 0:
                return curr.val
            curr = curr.right