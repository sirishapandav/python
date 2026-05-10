class Solution:
    def findCeil(self,root,x):
        ans=-1
        curr=root
        while curr:
            if curr.data==x:
                return curr.data
            elif curr.data>x:
                ans=curr.data
                curr=curr.left
            else:
                curr=curr.right
        return ans