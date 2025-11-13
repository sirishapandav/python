class Solution:
    def isBalanced(self,root:optional[treenode])->bool:
        def help(node):
            if not root:
                return 0
            l1=help(node.left)
            r1=help(node.right)
            if l1==-1 or r1==-1:
                return -1
            if abs(l1-r1)>1:
                return -1
            return 1+max(l1,r1)
        return help(root)!=1
