def generate(self,numrows: int)->list[list[int]]:
    res=[]
    for i in range(numrows):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=res[i-1][j-1]+res[i-1][j]
        res.append(row)
    return res        
numrows=5
print(generate)      