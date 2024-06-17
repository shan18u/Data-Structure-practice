class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        # HINT: we will use bfs and queue for this 
        # add root node to queue -> and once that level order is done then -> add the rightmost value pop it and add them to our result.
        res = []
        q = collections.deque([root])

        while q: # start level by level
            rightSide = None # if our its null
            qLen = len(q) # for 1st level get its length, ...

            for i in range(qLen):
                node = q.popleft() # pop to left and add to right
                if node: # if not null only then update our right-side to last node
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res