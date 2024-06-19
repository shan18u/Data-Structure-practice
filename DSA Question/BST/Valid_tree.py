class Solution:
    def isValidBST(self, root: TreeNode) -> bool: # return in boolean
        # Make sure that left side is only greater than all the nodes you have met on that specific sides, and other is opposite 
        # HINT: make sure that the reading node is btw inf and prev. visited node

        def valid(node, left, right):
            # base case
            if not node:
                return True
            # if this HINTED condition does not satisfy, then return false
            if not (left < node.val < right):
                return False

            # make recursive call, only when (node.left, left, node.val) => (less than, node, greater than) and opposite for right sub-trees
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf")) # set left boundary to -infm and right +inf