class Solution:
    def isSameTree(self,p,q: optional[TreeNode]):
        if not p and not q:
                return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        if p.val!=q.val:
            return False
        s1=self.isSameTree(p.left,q.left)
        s2=self.isSameTree(p.right,q.right)
        if s1 and s2:
            return True
        else:
            return False
            