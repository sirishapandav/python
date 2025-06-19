class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
def create_btree(arr,i,n):
        if i>n:
            return None
        root=TreeNode(arr[i-1])
        root.left=create_btree(arr,2*i,n)
        root.right=create_btree(arr,2*i+1,n)
        return root
arr=[3,4,5,6,7,8,9,0]
binary_tree=create_btree(arr,1,len(arr))
print(binary_tree)