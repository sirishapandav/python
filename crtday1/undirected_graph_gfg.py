class Solution:
    def isCycle(self, v, edges):
       
        # Step 1: Create adjacency list
        adj = [[] for _ in range(v)]
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)   # important for undirected graph
       
        visited = [0] * v
       
        # Step 2: DFS function
        def dfs(cur, prev):
            visited[cur] = 1
           
            for n in adj[cur]:
                if visited[n] == 0:
                    if dfs(n, cur):
                        return True
                elif n != prev:
                    return True
           
            return False
       
        # Step 3: Check all components
        for i in range(v):
            if visited[i] == 0:
                if dfs(i, -1):
                    return True
       
        return False
