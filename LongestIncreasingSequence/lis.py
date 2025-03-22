# Given an array arr[] of non-negative integers, the task is to find the length of the Longest Strictly Increasing Subsequence (LIS).

# A subsequence is strictly increasing if each element in the subsequence is strictly less than the next element.

# Examples:

# Input: arr[] = [5, 8, 3, 7, 9, 1]
# Output: 3
# Explanation: The longest strictly increasing subsequence could be [5, 7, 9], which has a length of 3.
# Input: arr[] = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# Output: 6
# Explanation: One of the possible longest strictly increasing subsequences is [0, 2, 6, 9, 13, 15], which has a length of 6.
# Input: arr[] = [3, 10, 2, 1, 20]
# Output: 3
# Explanation: The longest strictly increasing subsequence could be [3, 10, 20], which has a length of 3.

def lis(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

print(lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))  # 6
print(lis([48, 37, 41, 38, 2]))  # 3
print(lis([5, 8, 3, 7, 9, 1]))  # 3
print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))  # 6
print(lis([3, 10, 2, 1, 20]))  # 3
print(lis([3, 2]))  # 1
print(lis([3]))  # 1