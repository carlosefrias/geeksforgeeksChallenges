# Distance of nearest cell having 1
# Difficulty: MediumAccuracy: 47.7%Submissions: 108K+Points: 4Average Time: 20m
# Given a binary grid[][], where each cell contains either 0 or 1, find the distance of the nearest 1 for every cell in the grid.
# The distance between two cells (i1, j1)  and (i2, j2) is calculated as |i1 - i2| + |j1 - j2|. 
# You need to return a matrix of the same size, where each cell (i, j) contains the minimum distance from grid[i][j] to the nearest cell having value 1.

# Note: It is guaranteed that there is at least one cell with value 1 in the grid.

# Examples

# Input: grid[][] = [[0, 1, 1, 0], 
#                 [1, 1, 0, 0], 
#                 [0, 0, 1, 1]]
# Output: [[1, 0, 0, 1], 
#         [0, 0, 1, 1], 
#         [1, 1, 0, 0]]
# Explanation: The grid is -

# - 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and (2,1) are at a distance of 1 from 1's at (0,1), (0,2), (0,2), (2,3), (1,0) and (1,1) respectively.

# Input: grid[][] = [[1, 0, 1], 
#                 [1, 1, 0], 
#                 [1, 0, 0]]
# Output: [[0, 1, 0], 
#         [0, 0, 1], 
#         [0, 1, 2]]
# Explanation: The grid is -

# - 0's at (0,1), (1,2), (2,1) and (2,2) are at a  distance of 1, 1, 1 and 2 from 1's at (0,0), (0,2), (2,0) and (1,1) respectively.

# Constraints:
# 1 ≤ grid.size() ≤ 200
# 1 ≤ grid[0].size() ≤ 200

# Expected Complexities
# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)

from collections import deque

class Solution:
    def nearest(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        # Initialize result matrix with infinity
        res = [[float('inf')] * cols for _ in range(rows)]
        
        # Queue for BFS: stores (row, col, distance)
        queue = deque()
        
        # Initialize: all cells with 1 have distance 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res[i][j] = 0
                    queue.append((i, j, 0))
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS traversal
        while queue:
            row, col, dist = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if new position is valid
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    res[new_row][new_col] > dist + 1):
                    res[new_row][new_col] = dist + 1
                    queue.append((new_row, new_col, dist + 1))
        
        return res

sol = Solution()
grid = [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
print(sol.nearest(grid))


grid = [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
print(sol.nearest(grid))