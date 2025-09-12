def transpose(self,matrix:list[list[int]]):
    r,c=len(matrix),len(matrix[0])
    res=[[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            res[j][i]=matrix[i][j]
    return res        