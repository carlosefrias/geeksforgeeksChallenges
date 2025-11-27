# Path With Minimum Effort
# Difficulty: MediumAccuracy: 53.13%Submissions: 54K+Points: 4Average Time: 25m
# You are given a 2D array mat[][], of size n*m. Your task is to find the minimum possible path cost from the top-left cell (0, 0) to the bottom-right cell (n-1, m-1) by moving up, down, left, or right between adjacent cells.

# Note: The cost of a path is defined as the maximum absolute difference between the values of any two consecutive cells along that path.

# Examples:

# Input: mat[][] = [[7, 2, 6, 5],
#                [3, 1, 10, 8]]
# Output: 4
# Explanation: The route of [7, 3, 1, 2, 6, 5, 8] has a minimum value of maximum absolute difference between any two consecutive cells in the route, i.e., 4.
   
# Input: mat[][] = [[2, 2, 2, 1],
#                [8, 1, 2, 7],
#                [2, 2, 2, 8],
#                [2, 1, 4, 7],
#                [2, 2, 2, 2]]
# Output: 0
# Explanation: The route of [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] has a minimum value of maximum absolute difference between any two consecutive cells in the route, i.e., 0.
    
# Constraints:
# 1 ≤ n, m ≤ 100
# 0 ≤ mat[i][j] ≤ 106

# Expected Complexities
# Time Complexity: O(n * m log (n * m))
# Auxiliary Space: O(n * m)

import heapq
class Solution:
    def minCostPath(self, mat):
        if not mat or not mat[0]:
            return 0
        n, m = len(mat), len(mat[0])
        # Min-heap: (max_difference_so_far, row, col)
        heap = [(0, 0, 0)]
        # Track minimum max difference to reach each cell
        effort = [[float('inf')] * m for _ in range(n)]
        effort[0][0] = 0
        # Directions: up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while heap:
            current_effort, row, col = heapq.heappop(heap)
            # If reached destination
            if row == n - 1 and col == m - 1:
                return current_effort
            # If we found a better path to this cell already, skip
            if current_effort > effort[row][col]:
                continue
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m:
                    # Calculate the absolute difference
                    diff = abs(mat[nr][nc] - mat[row][col])
                    # The effort to reach neighbor is the maximum of current path effort and this edge
                    new_effort = max(current_effort, diff)
                    # If we found a better path to the neighbor
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        print(effort)
                        heapq.heappush(heap, (new_effort, nr, nc))
        return effort[n-1][m-1]

sol = Solution()
mat = [[7, 2, 6, 5], [3, 1, 10, 8]]
print(sol.minCostPath(mat))