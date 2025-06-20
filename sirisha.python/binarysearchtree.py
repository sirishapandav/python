class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def createbst(root, val):
    if root is None:
        return TreeNode(val)
    if val<root.data:
        root.left=createbst(root.left,val)
    elif val>root.data:
        root.right=createbst(root.right,val)
    return root
arr=[8,3,10,1,6,14,4,7]
root=TreeNode(arr[0])
for i in range(1,len(arr)):
     root=createbst(root,arr[i])
for val in arr:
    root=createbst(root,val)

def preorder(root):
        if root:
            print(root.data,end=" ")
            preorder(root.left)
            preorder(root.right)
print("Preorder traversal: ",end="")  
preorder(root)

def inorder(root):
        if root:
            inorder(root.left)
            print(root.data,end=" ")
            inorder(root.right)     
print("\nInorder traversal: ",end="")  
inorder(root) 

def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right) 
            print(root.data,end=" ")   
print("\nPostorder traversal: ",end="")  
postorder(root)  

def search(root, ele):
     if root is None:
          return False
     if root.data==ele:
          return True   
     elif ele<root.data:
          return search(root.left,ele)
     else:
          return search(root.right,ele)

def find_max(root):
     if root is None:
          return None
     while root.right:
          root=root.right
          return root.data
print(find_max(root))      

def find_min(root):
     if root is None:
          return None
     while root.left:
          root=root.left
          return root.data
print(find_min(root))     

def delete_node(root,key):
     if root is None:
          return root
     if key< root.data:
          root.left=delete_node(root.left,key)
     elif key>root.data:
          root.right=delete_node(root.right,key)
     else:
          if root.left is None:
               return root.right
          elif root.right is None:
               return root.left
          temp=find_min(root.right)
          root.data=temp.data
          root.right=delete_node(root.right,temp.data)
          return root             

def updaten(root,oldval,newval):
     root=delete_node(root,oldval)
     root=createbst(root,newval)
     return root

def find_floor(root,x):
     floor=None
     while root:
          if root.data==x:
               return root.data
          elif root.data>x:
               root=root.left
          else:
               floor=root.data
               root=root.right
     return floor
print(find_floor(root,11))

def find_ceil(root,x):
     ceil=None
     while root:
          if root.data==x:
               return root.data
          elif root.data<x:
               root=root.right
          else:
               ceil=root.data
               root=root.left
     return ceil               
print(find_ceil(root,11))         
              
arr=[8,3,10,1,6,14,4,7]
root=TreeNode(arr[0])
for i in range(1,len(arr)):
     root=createbst(root,arr[i])
print(f"\n\nsearch10:{search(root,10)}")     
    
 
 
     

 


