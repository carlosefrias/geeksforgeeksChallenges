# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], 
# where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

from collections import defaultdict

def is_cycle(V, edges):
    """
    Detects if an undirected graph contains a cycle using Depth First Search (DFS).

    Args:
        V (int): The number of vertices in the graph.
        edges (list of lists): A list of edges, where each edge is a list [u, v] representing an undirected edge between vertices u and v.

    Returns:
        bool: True if the graph contains a cycle, False otherwise.
    """

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * V

    def dfs(node, parent):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in range(V):
        if not visited[node]:
            if dfs(node, -1):
                return True

    return False
        
# Test cases
print(is_cycle(4, [[0, 1], [0, 2], [1, 2], [2, 3]])) # True
print(is_cycle(4, [[0, 1], [1, 2], [2, 3]]))    # False

# Examples:

# Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
# Output: true
# Explanation: 
 
# 1 -> 2 -> 0 -> 1 is a cycle.
# Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
# Output: false
# Explanation: 
 
# No cycle in the graph.
# Constraints:
# 1 ≤ V ≤ 105
# 1 ≤ E = edges.size() ≤ 105