class Solution:
    def isCyclic(self, v, edges):
        adj = [[] for _ in range(v)]
        for u, w in edges:
            adj[u].append(w)
           
        visited = [False]*v
        path = [False]*v
        def dfs(cur):
            visited[cur] = True
            path[cur] = True
            for ne in adj[cur]:
                if not visited[ne]:
                    if dfs(ne):
                        return True
                elif path[ne]:
                    return True
            path[cur] = False
            return False
           
        for i in range(v):
            if not visited[i]:
                if dfs(i):
                    return True
        return False
              