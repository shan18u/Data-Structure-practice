class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # we will use BFS and Queues to create a sublist of based on every level

        res = []    # array for the results
        q = collections.deque() # init queue

        if root:
            q.append(root) 
        
        # run bfs while q is not empty
        while q:
            val = []
            # iterate to one level at time
            for i in range(len(q)):
                
                # using fifo we will pop the node from the left
                node = q.popleft()
                val.append(node.val)
                # check if node is not null using if, cuz if we don't we could add null which we don't want 
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # after the entire level is done, we will add
            res.append(val)
        return res