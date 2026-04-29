class solution:
    def findOrder(self,n,prerequisties):
        #step1 creating adj list
        adj=[[] for i in range (n)]
        for s,d in prerequisties:
            adj[s].append(d)
        output=[]
        cycle,completed=set(),set()
        def dfs(cur):
            if cur in completed:
                return True
            if cur in cycle:
                return False
            cycle.add(cur)
            for ne in adj[cur]:
                dfs(ne)
            completed.add(cur)
            cycle.remove(cur)
            output.append(cur)    

        #call dfs for all course
        for c in range(n):
            if dfs(c)==False:  
                return[]  
        return output
  