# Nearly sorted
# Difficulty: MediumAccuracy: 75.25%Submissions: 80K+Points: 4Average Time: 30m
# Given an array arr[], where each element is at most k positions away from its correct position in the sorted order.
# Your task is to restore the sorted order of arr[] by rearranging the elements in place.

# Note: Don't use any sort() method.

# Examples:

# Input: arr[] = [2, 3, 1, 4], k = 2
# Output: [1, 2, 3, 4]
# Explanation: All elements are at most k = 2 positions away from their correct positions.
# Element 1 moves from index 2 to 0
# Element 2 moves from index 0 to 1
# Element 3 moves from index 1 to 2
# Element 4 stays at index 3
# Input: arr[]= [7, 9, 14], k = 1
# Output: [7, 9, 14]
# Explanation: All elements are already stored in the sorted order.
# Constraints:
# 1 ≤ arr.size() ≤ 106
# 0 ≤ k < arr.size()
# 1 ≤ arr[i] ≤ 106

# Expected Complexities
# Time Complexity: O(n log k)
# Auxiliary Space: O(k)

# class Solution:
#     def nearlySorted(self, arr, k):
#         # n = len(arr)
#         # if n == 0:
#         #     return arr
#         # if k == 0:
#         #     return arr
#         # def min(arr):
#         #     minimum = arr[0]
#         #     index = 0
#         #     n = len(arr)
#         #     for i in range(n):
#         #         val = arr[i]
#         #         if val < minimum:
#         #             minimum = val
#         #             index = i
#         #     return minimum, index
#         # pos = 0
#         # while pos < n:
#         #     part = arr[pos: pos + k + 1]
#         #     minimum, idx = min(part)
#         #     # swapping minimum to position
#         #     aux = arr[pos]
#         #     arr[pos] = minimum
#         #     arr[pos + idx] = aux
#         #     pos += 1
#         # return arr
#         n = len(arr)
#         if n <= 1 or k == 0:
#             return arr
            
#         for i in range(1, n):
#             key = arr[i]
#             j = i - 1
            
#             # Only check up to k positions back
#             while j >= max(0, i - k) and arr[j] > key:
#                 arr[j + 1] = arr[j]
#                 j -= 1
#             arr[j + 1] = key
                
        # return arr


import heapq

class Solution:
    def nearlySorted(self, arr, k):
        n = len(arr)
        if n <= 1 or k == 0:
            return arr
        
        # Min-heap to store the next k+1 elements
        heap = []
        
        # Add first k+1 elements to the heap (or all if n < k+1)
        for i in range(min(k + 1, n)):
            heapq.heappush(heap, arr[i])
        
        index = 0
        # Process remaining elements
        for i in range(k + 1, n):
            # Extract minimum from heap and place at current position
            arr[index] = heapq.heappop(heap)
            index += 1
            
            # Add next element to heap
            heapq.heappush(heap, arr[i])
        
        # Extract remaining elements from heap
        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1
            
        return arr


sol = Solution()
print(sol.nearlySorted([2, 3, 1, 4], 2))