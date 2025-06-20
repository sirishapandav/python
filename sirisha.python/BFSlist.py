def bfs_list(graph,start):
    n=len(graph)
    queue=[start]
    visited=[False]*n
    visited[start]=1
    while queue:
        node=queue.pop()
        print(node,end=" ")
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj]=1
                queue.append(adj)
graph={0:[1,2],1:[2],2:[0,3],3:[3]}
bfs_list(graph,1)
