def dfs_mat(graph,start,visited=None):
    if visited is None:
        visited=set()
        visited.add(start)
        visited.add(start)
        print(start,end=" ")
        for adj in graph[start]:
            if adj not in visited:
                dfs_mat(graph,adj,visited)
graph=[
    [1,2],
    [2],
    [0,3],
    [3],
] 
dfs_mat(graph,0)  
