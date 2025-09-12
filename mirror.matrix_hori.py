def hori(mat):
    for row in mat:
        l=0
        r=len(row)-1
        while l<r:
            row[l],row[r]=row[r],row[l]
            l+=1
            r-=1
    return mat
mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]
print(hori(mat))