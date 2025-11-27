# Number of BST From Array
# Difficulty: HardAccuracy: 87.95%Submissions: 2K+Points: 8
# You are given an integer array arr[] containing distinct elements.

# Your task is to return an array where the ith element denotes the number of unique BSTs formed when arr[i] is chosen as the root.

# Examples :

# Input: arr[] = [2, 1, 3]
# Output: [1, 2, 2]
# Explanation: 
# 4
# Input: arr[] = [2, 1]
# Ouput: [1, 1]
# Constraints:
# 1 ≤ arr.size() ≤ 6
# 1 ≤ arr[i] ≤ 15

# Expected Complexities
# Time Complexity: O(n log n)
# Auxiliary Space: O(n)

class Solution:
    def countBSTs(self, arr):
        # Code here
        n = len(arr)
        
        # Sort the array to get ordering
        sorted_arr = sorted(arr)
        
        # Precompute Catalan numbers up to n
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        # Create result array
        result = []
        
        # For each element, find its position in sorted array
        for num in arr:
            # Find index in sorted array to determine left/right subtree sizes
            idx = sorted_arr.index(num)
            left_size = idx
            right_size = n - idx - 1
            result.append(catalan[left_size] * catalan[right_size])
        return result

sol = Solution()

result = sol.countBSTs([2,1,3])
print(result)

result = sol.countBSTs([2,1])
print(result)


result = sol.countBSTs([3,4,1,2,5])
print(result)