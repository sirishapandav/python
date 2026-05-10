class solution:
    def preorderTraversal(self,root: Optional[Treenode]):
        if not root:
            return[]
        res=[]
        st=[root]
        while st:
            node=st.pop()
            res.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return res