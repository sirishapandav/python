def bfs_matrix(graph,start):
    n=len(graph)
    queue=[start]
    visited=[False]*n
    visited[start]=1
    while queue:
        node=queue.pop(0)
        print(node,end=" ")
        for adj in range (n):
            if graph[node][adj]!=False and visited[adj]==False:
                visited[adj]=1
                queue.append(adj)
graph=[
    [0,1,1,1],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,0,1],
]                
bfs_matrix(graph,1)