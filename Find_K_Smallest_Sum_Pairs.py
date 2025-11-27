# Find K Smallest Sum Pairs
# Difficulty: MediumAccuracy: 40.0%Submissions: 35+Points: 4
# Given two integer arrays arr1[] and arr2[] sorted in ascending order and an integer k, your task is to find k pairs with the smallest sums, such that one element of each pair belongs to arr1[] and the other belongs to arr2[].

# Return the list of these k pairs, where each pair is represented as [arr1[i], arr2[j]].

# Note: You can return any possible k pairs with the smallest sums, the driver code will print true if it is correct else it will print false.

# Examples:

# Input: arr1[] = [1, 7, 11], arr2[] = [2, 4, 6], k = 3
# Output: true
# Explanation: All possible combinations of elements from the two arrays are:
# [1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [7, 6], [11, 2], [11, 4], [11, 6]. 
# Among these, the three pairs with the minimum sums are [1, 2], [1, 4], [1, 6].
# Input: arr1[] = [1, 3], arr2[] = [2, 4] k = 2
# Output: true
# Explanation: All possible combinations are [1, 2], [1, 4], [3, 2], [3, 4]. 
# Among these, the two pairs with the minimum sums are [1, 2], [3, 2].
# Constraints:
# 1 ≤ arr1.size(), arr2.size() ≤ 5*104
# 1 ≤ arr1[i], arr2[j] ≤ 109
# 1 ≤ k ≤ 103

# Expected Complexities
# Time Complexity: O(k*log k)
# Auxiliary Space: O(k)

import heapq

class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        if not arr1 or not arr2 or k == 0:
            return []
        
        # Min heap: (sum, arr1_value, arr2_value, index_in_arr1, index_in_arr2)
        heap = []
        visited = set()
        
        # Push the first pair (smallest possible sum)
        heapq.heappush(heap, (arr1[0] + arr2[0], arr1[0], arr2[0], 0, 0))
        visited.add((0, 0))
        
        result = []
        
        while heap and len(result) < k:
            # Get the smallest sum pair
            current_sum, val1, val2, i, j = heapq.heappop(heap)
            result.append([val1, val2])
            
            # Generate next possible pairs
            # Next element from arr1 with same arr2 element
            if i + 1 < len(arr1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (arr1[i + 1] + arr2[j], arr1[i + 1], arr2[j], i + 1, j))
                visited.add((i + 1, j))
            
            # Next element from arr2 with same arr1 element  
            if j + 1 < len(arr2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (arr1[i] + arr2[j + 1], arr1[i], arr2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        
        return result

sol = Solution()
arr1 = [8, 10, 10, 11, 12, 13, 13, 13]
arr2 = [5, 6, 8, 10, 13]
k = 4
res = sol.kSmallestPair(arr1, arr2, k)
print(res)