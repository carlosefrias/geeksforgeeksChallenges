# Top K Frequent in Array
# Difficulty: MediumAccuracy: 40.23%Submissions: 102K+Points: 4Average Time: 30m
# Given a non-empty integer array arr[]. Your task is to find and return the top k elements which have the highest frequency in the array.

# Note: If two numbers have the same frequency, the larger number should be given the higher priority.

# Examples:

# Input: arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
# Output: [4, 1]
# Explanation: Frequency of 4 is 2 and frequency of 1 is 2, these two have the maximum frequency and 4 is larger than 1.
# Input: arr[] = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
# Output: [5, 11, 7, 10]
# Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, frequency of 10 is 1.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105
# 1 ≤ k ≤ no. of distinct elements

# Expected Complexities
# Time Complexity: O(n log n)
# Auxiliary Space: O(n)

class Solution:
    def topKFreq(self, arr, k):
        dic = {}
        for val in arr:
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1
        n = len(arr)
        buckets = [[] for _ in range(n + 1)]
        
        for key, value in dic.items():
            buckets[value].append(key)
        
        sol = []
        while n >= 0 and len(sol) < k:
            values = buckets[n]
            if len(values) > 0:
                values.sort(reverse=True)
                for v in values:
                    sol.append(v)
                    if(len(sol) >= k):
                        break
            n -= 1
        return sol[:k]


sol = Solution()

res = sol.topKFreq([3, 1, 4, 4, 5, 2, 6, 1], 2)
print(res)

res = sol.topKFreq([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4)
print(res)