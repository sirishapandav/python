class solution:
    def jobsequencing(self,deadline,profit):
        mat=[]
        id=1
        for i in range (0,len(deadline)):
            mat.append([id,deadline[i],profit[i]])
            id+=1
        mat.sort(key=lambda x:-x[2])
        maxdeadline=-1
        for row in range(0,len(mat)):
            maxdeadline=max(maxdeadline,mat[row][1])
        days=[-1]*(maxdeadline+1)
        maxProfit=0
        cnt=0
        for row in range(0,len(mat)):
            for j in range(mat[row][1],0,-1):
                if(days[j]==-1):
                    days[j]=mat[row][0]
                    maxProfit+=mat[row][2]
                    cnt+=1
                    break
        return[cnt,maxProfit]               

    