# You are given an undirected weighted graph with V vertices numbered from 0 to V-1 and E edges, represented as a 2D array edges[][], where edges[i] = [ui, vi, timei] means that there is an undirected edge between nodes ui and vi that takes timei minutes to reach.
# Your task is to return in how many ways you can travel from node 0 to node V - 1 in the shortest amount of time.

# Examples:

# Input: V = 4, edges[][] = [[0, 1, 2], [1, 2, 3], [0, 3, 5], [1, 3, 3], [2, 3, 4]]
    
# Output: 2
# Explanation: The shortest path from 0 to 3 is 5.
# Two ways to reach 3 in 5 minutes are:
# 0 -> 3
# 0 -> 1 -> 3
# Input: V = 6, edges[][] = [[0, 2, 3], [0, 4, 2], [0, 5, 7], [2, 3, 1], [2, 5, 5], [5, 3, 3], [5, 1, 4], [1, 4, 1], [4, 5, 5]]
    
# Output: 4
# Explanation: The shortest path from 0 to 5 is 7.
# Four ways to reach 5 in 7 minutes are:
# 0 -> 5
# 0 -> 4 -> 5
# 0 -> 4 -> 1 -> 5
# 0 -> 2 -> 3 -> 5
# Constraints:
# 1 ≤ V ≤ 200
# V - 1 ≤ edges.size() ≤ V * (V - 1) / 2
# 0 ≤ ui, vi ≤ V - 1
# 1 ≤ timei ≤ 105
# ui != vi

# Expected Complexities
# Time Complexity: O(V + E * log E)
# Auxiliary Space: O(V + E)

class MySolution:
    def countPaths(self, V, edges):
        path = [0]
        results = []
        minimum = float('inf')

        def dfs(vertex, V, edges, path, time):
            nonlocal minimum
            if vertex == V-1:
                if time < minimum:
                    minimum = time
                results.append((path.copy(), time))
                return
            for edge in edges:
                if edge[0] == vertex and edge[1] not in path:
                    path.append(edge[1])
                    time += edge[2]
                    if time <= minimum:
                        dfs(edge[1], V, edges, path, time)
                    path.pop()
                    time -= edge[2]
                if edge[1] == vertex and edge[0] not in path:
                    path.append(edge[0])
                    time += edge[2]
                    if time <= minimum:
                        dfs(edge[0], V, edges, path, time)
                    path.pop()
                    time -= edge[2]

        dfs(0, V, edges, path, 0)
        count = 0
        for result in results:
            if result[1] == minimum:
                count += 1
        return count



import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7
        # build adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float('inf')] * V
        ways = [0] * V
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (distance, node)
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(heap, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[V - 1] % MOD


sol = Solution()
V = 4
edges = [[0, 1, 2], [1, 2, 3], [0, 3, 5], [1, 3, 3], [2, 3, 4]]

print(sol.countPaths(V, edges))

V = 6
edges = [[0, 2, 3], [0, 4, 2], [0, 5, 7], [2, 3, 1], [2, 5, 5], [5, 3, 3], [5, 1, 4], [1, 4, 1], [4, 5, 5]]

print(sol.countPaths(V, edges))