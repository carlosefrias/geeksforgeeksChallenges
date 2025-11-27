# You are given an integer n, there is a n × n chessboard with a Knight starting at the top-left corner (0, 0). Your task is to determine a valid Knight's Tour, where the Knight visits every square exactly once, following the standard movement rules of a chess Knight (two steps in one direction and one step perpendicular), for example if a Knight is placed at cell (2, 2), in one move it can move to any of the following cells: (4, 3), (4, 1), (0, 3), (0, 1), (3, 4), (3, 0), (1, 4) and (1, 0).

# You have to return the order in which each cell is visited. If a solution exists, return the sequence of numbers (starting from 0) representing the order of visited squares. If no solution is possible, return an empty list.

# Note: You can return any valid ordering, if it is correct the driver code will print true else it will print false.

# Examples:

# Input: n = 5
# Output: true
# Explanation: A possible Knight's Tour in a 5x5 chessboard is given below where Each number represents the step at which the Knight visits that cell, starting from (0, 0) as step 0.
# [[0, 11, 2, 17, 20],
#  [3, 16, 19, 12, 7],
#  [10, 1, 6, 21, 18],
#  [15, 4, 23, 8, 13], 
#  [24, 9, 14, 5, 22]]
# Input: n = 4
# Output: true
# Explanation: For n = 4, it is not possible for a valid Knight's Tour so you have to return [].
# Constraints:
# 1 ≤ n ≤ 6

# Expected Complexities
# Time Complexity: O(8 ^ (n * n) )
# Auxiliary Space: O(n^2)


class Solution:
    def knightTour(self, n):
        # Check if solution is possible (for n=1,2,3,4 it might not be possible)
        if n == 1:
            return [[0]]
        if n <= 3:  # No solution exists for n=2,3
            return []
        if n == 4:  # No solution exists for standard chessboard
            return []
        
        # All possible knight moves
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        
        # Initialize board
        board = [[-1 for _ in range(n)] for _ in range(n)]
        
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n and board[x][y] == -1
        
        def solve(x, y, move_count):
            # Mark current cell
            board[x][y] = move_count
            
            # If all cells are visited, we found a solution
            if move_count == n * n - 1:
                return True
                
            # Try all possible moves from current position
            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy
                if is_valid(next_x, next_y):
                    if solve(next_x, next_y, move_count + 1):
                        return True
            
            # Backtrack: if no move leads to solution, unmark this cell
            board[x][y] = -1
            return False
        
        # Start from (0, 0)
        if solve(0, 0, 0):
            return board
        else:
            return []

sol = Solution()

print(sol.knightTour(10))