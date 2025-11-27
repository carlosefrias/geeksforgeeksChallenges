# Rat in a Maze
# Difficulty: MediumAccuracy: 35.75%Submissions: 384K+Points: 4Average Time: 25m
# Consider a rat placed at position (0, 0) in an n x n square matrix maze[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

# The matrix contains only two possible values:

# 0: A blocked cell through which the rat cannot travel.
# 1: A free cell that the rat can pass through.
# Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
# If no path exists, return an empty list.

# Note: Return the final result vector in lexicographically smallest order.

# Examples:

# Input: maze[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
# Output: ["DDRDRR", "DRDDRR"]
# Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.
# Input: maze[][] = [[1, 0], [1, 0]]
# Output: []
# Explanation: No path exists as the destination cell (1, 1) is blocked.
# Input: maze[][] = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# Output: ["DDRR", "RRDD"]
# Explanation: The rat has two possible paths to reach the destination: DDRR and RRDD.
# Constraints:
# 2 ≤ n ≤ 5
# 0 ≤ maze[i][j] ≤ 1

# Expected Complexities
# Time Complexity: O(4 ^ (n * n))
# Auxiliary Space: O(n * n)

class Solution:
    def ratInMaze(self, maze):
        # code here
        # Correct move deltas: (dx, dy) where dx changes row index, dy changes column index
        moves = {"D": (1, 0), "L": (0, -1), "R": (0, 1), "U": (-1, 0)}
        n = len(maze)

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

        results = []

        def dfs(x, y, path):
            # If reached destination, record the path
            if x == n - 1 and y == n - 1:
                results.append("".join(path))
                return

            # mark visited
            maze[x][y] = 0
            # iterate moves (order doesn't matter since we sort at the end)
            for key in moves:
                dx, dy = moves[key]
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    path.append(key)
                    dfs(nx, ny, path)
                    path.pop()
            # backtrack visited
            maze[x][y] = 1

        # Start from (0, 0)
        if n == 0 or maze[0][0] == 0:
            return []

        dfs(0, 0, [])
        results.sort()
        return results

sol = Solution()
 
print(sol.ratInMaze([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]))


