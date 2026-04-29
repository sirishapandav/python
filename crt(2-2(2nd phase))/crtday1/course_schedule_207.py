class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for i in range(numCourses)]
        for s,d in prerequisites:
            adj[s].append(d)
        visited =  set()
        def dfs(cur):
            if cur in visited:
                return False  
            if adj[cur]  == []:
                return True
            visited.add(cur)
            for ne in adj[cur]:
                if not dfs(ne):
                    return False
            adj[cur] = []
            visited.remove(cur)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
