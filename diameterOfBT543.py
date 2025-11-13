class Solution:
    def diameterOfBinaryTree(self):
        self.diameter=0
        def help(node):
            if not node:
                return 0
            l1=help(node.left)
            r1=help(node.right)
            slef.diameter=max(self.daiameter,l1+r1)
            return 1+max(l1,r1)
        help(root)
        return self.diameter