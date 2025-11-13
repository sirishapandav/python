class Solution:
    def isSymmetric(self,root:optional[treenode]):
        def help(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val!=t2.val:
                rteurn False
            lmirror=help(t1.left,t2.right)
            lmirror=help(t1.right,t2.left)
            if lmirror and rmirror:
                return True
            else:
                return False
        return help(root.left,root.right)    

            
            