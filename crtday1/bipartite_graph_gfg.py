class Solution:
    def isBipartite(self, v, edges):
       
        adj = [[] for i in range(v)]
        for s,d in edges:
            adj[s].append(d)
       
        c = [-1] *v
       
        for i in range(v):
            if c[i] == -1:
           
                queue = [i]
                front = 0
                c[i] = 0  
               
                while front < len(queue):
                    cur = queue[front]
                    for ne in adj[cur]:
                        if c[ne] == -1:
                            c[ne] =  1 - c[cur]
                            queue.append(ne)
                        elif c[cur]  == c[ne]:
                            return False
                    front+=1
                return True
