class solution:
     def directedgraph(self,V,edges):
        adj=[[] for i in range(V)]
        ind=[0]*V
        for u,v in edges:
            adj[u].append(v)
            ind[v]+=1
        q=[]
        for i in range(V):
            if ind[i]==0:
                q.append(i)
        res=[]
        while q:
            node=q.pop(0)
            res.append(node)
            for nei in adj[node]:
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        return len(res)!=V