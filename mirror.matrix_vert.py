def vert(mat):
    top=0
    bottom=len(mat)-1
    while top<bottom:
        mat[top],mat[bottom]=mat[bottom],mat[top]
        top+=1
        bottom-=1
    
    return mat
mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]
print(vert(mat))