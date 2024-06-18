class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # recursive approach
        def dfs(node, maxVal):
            # empty node will return 0
            if not node:
                return 0

            # if good node then we get res = 1, else 0
            res = 1 if node.val >= maxVal else 0
            
            # update maxval, why cuz we need to pass new maxval to the recursive dfs call for the next iteration
            maxVal = max(maxVal, node.val)

            # count the new good nodes to our res
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)