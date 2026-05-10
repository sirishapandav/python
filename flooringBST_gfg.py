class Solution:
    def findMaxFork(self,root,k):
        ans=-1
        curr=root
        while curr:
            if curr.data==k:
                return curr.data
            elif curr.data<k:
                ans=curr.data
                curr=curr.right
            else:
                curr=curr.left
        return ans