# Pseudocode
# A recursive implementation of DFS:[5]

# procedure DFS(G, v) is
#     label v as discovered
#     for all directed edges from v to w that are in G.adjacentEdges(v) do
#         if vertex w is not labeled as discovered then
#             recursively call DFS(G, w)
# A non-recursive implementation of DFS with worst-case space complexity 

# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

# Given a connected undirected graph represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i.
# Perform a Depth First Search (DFS) traversal starting from vertex 0, visiting vertices from left to right as per the given adjacency list, and return a list containing the DFS traversal of the graph.

# Note: Do traverse in the same order as they are in the given adjacency list.
            
def dfs_recur(adj):
    def dfs_alg(graph, vertex):
        visited[vertex] = True
        result.append(vertex)
        for w in graph[vertex]:
            if not visited[w]:
                dfs_alg(graph, w)
    n = len(adj)
    visited = [False] * n 
    result = []
    dfs_alg(adj, 0)
    return result
    
print(dfs_recur([[2, 3, 1], [0], [0, 4], [0], [2]]))
print(dfs_recur([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]))

# or
# procedure DFS_iterative(G, v) is
#     let S be a stack
#     S.push(v)
#     while S is not empty do
#         v = S.pop()
#         if v is not labeled as discovered then
#             label v as discovered
#             for all edges from v to w in G.adjacentEdges(v) do
#                 if w is not labeled as discovered then
#                     S.push(w)