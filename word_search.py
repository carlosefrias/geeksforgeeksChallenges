# Word Search
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

class Solution:
    def exist(self, board, word):
        import collections

        rows, cols = len(board), len(board[0])

        # Quick impossible checks
        if len(word) > rows * cols:
            return False
        board_counts = collections.Counter(ch for row in board for ch in row)
        word_counts = collections.Counter(word)
        for ch, cnt in word_counts.items():
            if board_counts.get(ch, 0) < cnt:
                return False

        visited = [[False] * cols for _ in range(rows)]
        moves = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r, c, i):
            # i is index in word; board[r][c] should match word[i]
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited[r][c] = True
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if dfs(nr, nc, i + 1):
                        visited[r][c] = False
                        return True
            visited[r][c] = False
            return False

        first = word[0]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == first:
                    if dfs(r, c, 0):
                        return True
        return False

sol = Solution()
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCCED"
# print(sol.exist(board, word))

board = [["a","a"]]
word = "aaa"
print(sol.exist(board, word))