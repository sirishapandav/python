class Solution:
    def topoSort(self, v, edges):
       
        adj = [ [] for i in range(v)]
        for s,d in edges:
            adj[s].append(d)
        stack = []
        visited = [False ]*v
        def dfs(cur):
            visited[cur] = True
            for ne in adj[cur]:
                if not visited[ne]:
                    dfs(ne)
            stack.append(cur)
           
        for i in range(v):
            if not visited[i]:
                dfs(i)
        return stack[::-1]
