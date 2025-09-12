class solution:
    def rotate(self,matrix: list[list[int]])->list:

        n=len(matrix)
        for i in range(n):
             for j in range(i+1,n):
                 matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()        