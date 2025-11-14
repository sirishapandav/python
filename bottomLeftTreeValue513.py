class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
       q=[root]
       lm=root.val
       while q:
        for i in range(len(q)):
            node=q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i==0:
                lm=node.val
       return lm                
    