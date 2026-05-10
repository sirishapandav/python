class solution:
    def eventualSafeNodes(self,graph):
        n=len(graph)
        v=[o]*n
        pv=[0]*n
        safe=[0]*n
        def dfs(node):
            v[node]=1
            pv[node]=1
            for nei in graph[node]:
                if v[nei]==0:
                    if dfs(nei):
                        return True
                elif pv[nei]==1:
                    return True
            safe[node]=1
            pv[node]=0
            return False
        for i in range(n):
            if v[i]==0:
                dfs(i)
        res=[]
        for i in range(n):
            if safe[i]==1:
                res.append(i)
        return res