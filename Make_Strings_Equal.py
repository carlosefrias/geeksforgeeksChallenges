# Make Strings Equal
# Difficulty: MediumAccuracy: 60.22%Submissions: 4K+Points: 4
# Given two strings s and t, consisting of lowercase English letters. You are also given, a 2D array transform[][], where each entry [x, y] means that you are allowed to transform character x into character y and an array cost[], where cost[i] is the cost of transforming transform[i][0] into transform[i][1]. You can apply any transformation any number of times on either string.

# Your task is to find the minimum total cost required to make the strings identical. If it is impossible to make the two strings identical using the available transformations, return -1.

# Examples:

# Input: s = "abcc", t = "bccc", transform[][] = [['a', 'b'], ['b', 'c'], ['c', 'a']], cost[] = [2, 1, 4]
# Output: 3
# Explanation: We can convert both strings into "bccc" with a cost of 3 using these operations:
# transform at Position 0 in s: a -> b (cost 2)
# transform at Position 1 in s: b -> c (cost 1)
# Other characters already match.
# Input: s = "az", t = "dc", transform[][] = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['a', 'd'], ['z', 'c']], cost[] = [5, 3, 2, 50, 10]
# Output: 20
# Explanation: We can convert both strings into "dc" with a cost of 20 using these operations:
# transform at Position 0 in s: a -> d by path a -> b -> c -> d (cost 5 + 3 + 2 = 10)
# transform at Position 1 in s: z -> c (cost 10)
# Input: s = "xyz", t = "xzy", transform[][] = [['x', 'y'], ['x', 'z']], cost[] = [3, 3]
# Output: -1
# Explanation: It is not possible to make the two strings equal.
# Constraints:
# 1 ≤ s.size() = t.size() ≤ 105
# 1 ≤ transform.size() = cost.size() ≤ 500
# 'a' ≤ transform[i][0], transform[i][1] ≤ 'z'
# 1 ≤ cost[i] ≤ 500

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
    def minCost(self, s, t, transform, cost):
        # code here
        # Use Floyd–Warshall on the 26 letters to compute all-pairs minimal transform costs
        if len(s) != len(t):
            return -1

        ALPH = 26
        INF = float('inf')
        dist = [[INF] * ALPH for _ in range(ALPH)]
        for i in range(ALPH):
            dist[i][i] = 0

        # fill direct transformations (directed)
        for i in range(len(transform)):
            src_c, dst_c = transform[i]
            u = ord(src_c) - ord('a')
            v = ord(dst_c) - ord('a')
            dist[u][v] = min(dist[u][v], cost[i])

        # Floyd–Warshall
        for k in range(ALPH):
            dk = dist[k]
            for i in range(ALPH):
                di = dist[i]
                via = di[k]
                if via == INF:
                    continue
                # inline loop for speed
                for j in range(ALPH):
                    nd = via + dk[j]
                    if nd < di[j]:
                        di[j] = nd
        total_cost = 0
        n = len(s)
        for i in range(n):
            a = ord(s[i]) - ord('a')
            b = ord(t[i]) - ord('a')
            if a == b:
                continue
            best = INF
            # choose a common target letter k minimizing dist[a][k] + dist[b][k]
            for k in range(ALPH):
                da = dist[a][k]
                db = dist[b][k]
                if da == INF or db == INF:
                    continue
                cand = da + db
                if cand < best:
                    best = cand
            if best == INF:
                return -1
            total_cost += best
        return total_cost

sol = Solution()

s = "abcc"; t = "bccc"; transform = [['a', 'b'], ['b', 'c'], ['c', 'a']]; cost = [2, 1, 4]
print(sol.minCost(s, t, transform, cost))

s = "az"; t = "dc"; transform = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['a', 'd'], ['z', 'c']]; cost = [5, 3, 2, 50, 10]
print(sol.minCost(s, t, transform, cost))

s = "xyz"; t = "xzy"; transform = [['x', 'y'], ['x', 'z']]; cost = [3, 3]
print(sol.minCost(s, t, transform, cost))