# https://www.geeksforgeeks.org/problems/rotten-oranges2536/1
# Given a matrix mat[][] of dimension n * m where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
# 0 : Empty cell
# 1 : Cell have fresh oranges
# 2 : Cell have rotten oranges

# We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

# Note: Your task is to return the minimum time to rot all the fresh oranges. If not possible returns -1.

from collections import deque

def oranges_rotting(mat):
    n = len(mat)
    m = len(mat[0])
    queue = deque()
    fresh_count = 0

    # Initialize the queue with all rotten oranges and count fresh oranges
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif mat[i][j] == 1:
                fresh_count += 1

    # Directions for adjacent cells (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_time = 0

    # BFS to rot adjacent fresh oranges
    while queue:
        row, col, time = queue.popleft()
        max_time = max(max_time, time)

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                mat[nr][nc] = 2  # Mark as rotten
                fresh_count -= 1
                queue.append((nr, nc, time + 1))

    # If there are still fresh oranges, return -1
    return max_time if fresh_count == 0 else -1


print(oranges_rotting([[0, 1, 2], [0, 1, 2], [2, 1, 1]])) # 4
print(oranges_rotting([[2, 2, 0, 1]])) # -1
print(oranges_rotting([[2, 2, 2], [0, 2, 0]])) # 0
print(oranges_rotting([[2, 2, 0, 0, 1, 1]])) # -1
print(oranges_rotting([[2, 1, 0], [1, 1, 0], [0, 1, 1]])) # 4

# Examples:

# Input: mat[][] = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
# Output: 1
# Explanation: Oranges at positions (0,2), (1,2), (2,0) will rot oranges at (0,1), (1,1), (2,2) and (2,1) in unit time.
# Input: mat[][] = [[2, 2, 0, 1]]
# Output: -1
# Explanation: Oranges at (0,0) and (0,1) can't rot orange at (0,3).
# Input: mat[][] = [[2, 2, 2], [0, 2, 0]]
# Output: 0
# Explanation: There is no fresh orange. 
# Constraints:
# 1 ≤ mat.size() ≤ 500
# 1 ≤ mat[0].size() ≤ 500
# mat[i][j] = {0, 1, 2}