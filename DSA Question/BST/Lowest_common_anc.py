class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":


        # run the loop
        while True:
            # if root value is less than both p and q, then go to right
            if root.val < p.val and root.val < q.val:
                root = root.right
            # opposite
            elif root.val > p.val and root.val > q.val:
                root = root.left
            # else means we have found our results
            else:
                return root

























