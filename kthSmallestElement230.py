class Solution:
    def kthsmallest(self,root:optional[treenode],k:int)->int:
        c=0
        res=None
        def inorder(root):
            nonlocal c
            nonlocal res
            if root:
                inorder(root.left)
                c+=1
                if c==k:
                    res=root.val
                inorder(root.right)
        inorder(root)
        return res        
                
            
