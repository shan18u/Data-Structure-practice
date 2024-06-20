class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # make a tree node that will have first value of the preorder array, check doc, and get index
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # create both left and right subtree, by recursive, preorder -> get no. of node using mid, same for right
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
        # Recomend try this again using other language maybe java to get more in-depth code of build
