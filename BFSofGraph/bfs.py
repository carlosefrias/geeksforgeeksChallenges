# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

# Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. 
# Perform a Breadth First Search (BFS) traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list, and return a list containing the BFS traversal of the graph.

# Note: Do traverse in the same order as they are in the given adjacency list.

from queue import Queue

def bfs(adj):
    n = len(adj)
    if n == 0:
        return []
    
    visited = [False] * n
    is_or_was_in_queue = [False] * n
    q = Queue()
    q.put(0)
    is_or_was_in_queue[0] = True
    res = []
    while not q.empty():
        current = q.get()
        res.append(current)
        visited[current] = True
        for w in adj[current]:
            if not visited[w] and not is_or_was_in_queue[w]:
                q.put(w)
                is_or_was_in_queue[w] = True
    return res


print(bfs([[2, 3, 1], [0], [0, 4], [0], [2]]))
print(bfs([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]))
print(bfs([[3,5,6,7], [7], [6,4,7], [0,8], [2],[0],[8,0,2],[2,0,1,9],[3,6],[7]]))


# Examples:

# Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

# Output: [0, 2, 3, 1, 4]
# Explanation: Starting from 0, the BFS traversal will follow these steps: 
# Visit 0 → Output: 0 
# Visit 2 (first neighbor of 0) → Output: 0, 2 
# Visit 3 (next neighbor of 0) → Output: 0, 2, 3 
# Visit 1 (next neighbor of 0) → Output: 0, 2, 3, 
# Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4
# Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

# Output: [0, 1, 2, 3, 4]
# Explanation: Starting from 0, the BFS traversal proceeds as follows: 
# Visit 0 → Output: 0 
# Visit 1 (the first neighbor of 0) → Output: 0, 1 
# Visit 2 (the next neighbor of 0) → Output: 0, 1, 2 
# Visit 3 (the first neighbor of 2 that hasn't been visited yet) → Output: 0, 1, 2, 3 
# Visit 4 (the next neighbor of 2) → Final Output: 0, 1, 2, 3, 4