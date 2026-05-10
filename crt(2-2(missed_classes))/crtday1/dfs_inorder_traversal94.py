#iteration approach#
class soution:
    def inorderTraversal(self,root):
        res=[]
        st=[]
        curr=root
        while curr or st:
            while curr:
                st.append(curr)
                curr=curr.left
            curr=st.pop()
            res.append(curr.val)
            curr=curr.right
        return res        