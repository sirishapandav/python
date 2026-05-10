class solution:
    def buildTree(self, preorder:list[int],inorder):
        mapp={}
        for i in range(len(inorder)):
            mapp[inorder[i]]=i
        self.i=0
        def helper(left,right):
            if left>right:
                return None
            rootv=preorder[self.i]
            self.i+=1
            root=TreeNode(rootv)
            mid=mapp[rootv]
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(inorder)-1)