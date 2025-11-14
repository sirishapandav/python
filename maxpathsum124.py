class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float('-inf')
        def findmax(node):
            if not node:
                return 0
            l1=max(0,findmax(node.left))
            r1=max(0,findmax(node.right))
            curr=node.val+l1+r1
            self.maxsum=max(self.maxsum,curr)
            return node.val+max(l1,r1)
        findmax(root)
        return self.maxsum

        