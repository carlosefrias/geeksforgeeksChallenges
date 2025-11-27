# K Closest Points to Origin
# Difficulty: MediumAccuracy: 62.4%Submissions: 26K+Points: 4
# Given an integer k and an array of points points[][], where each point is represented as points[i] = [xi, yi] on the X-Y plane. Return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance, defined as:
# distance = sqrt( (x2 - x1)2 + (y2 - y1)2 )

# Note: You can return the k closest points in any order, the driver code will print them in sorted order.
# Test Cases are generated such that there will be a unique ans.

# Examples:

# Input: k = 2, points[] = [[1, 3], [-2, 2], [5, 8], [0, 1]]
# Output: [[-2, 2], [0, 1]]
# Explanation: The Euclidean distances from the origin are:
# Point (1, 3) = sqrt(10)
# Point (-2, 2) = sqrt(8)
# Point (5, 8) = sqrt(89)
# Point (0, 1) = sqrt(1)
# The two closest points to the origin are [-2, 2] and [0, 1].
# Input: k = 1, points = [[2, 4], [-1, -1], [0, 0]]
# Output: [[0, 0]]
# Explanation: The Euclidean distances from the origin are:
# Point (2, 4) = sqrt(20)
# Point (-1, -1) = sqrt(2)
# Point (0, 0) = sqrt(0)
# The closest point to origin is (0, 0).
# Constraints:
# 1 ≤ k ≤ points.size() ≤ 105
# -3*104 ≤ xi, yi ≤ 3*104

# Expected Complexities
# Time Complexity: O(n log k)
# Auxiliary Space: O(k)

class Solution:
    def kClosest(self, points, k):
        def squaredDistance(point):
            return point[0] * point[0] + point[1] * point[1]

        # code here
        n = len(points)
        distances = [ squaredDistance(point) for point in points]

        buckets = {}
        for i in range(n):
            distance = distances[i]
            if distance in buckets:
                buckets[distance].append(points[i])
            else:
                buckets[distance] = [points[i]]
        result = []
        distances.sort()
        count = 0
        for key in distances:
            for point in buckets[key]:
                result.append(point)
                count += 1
                if count == k:
                    return result
        return result


sol = Solution()

res = sol.kClosest([[1, 3], [-2, 2], [5, 8], [0, 1]], 2)
print(res)
        