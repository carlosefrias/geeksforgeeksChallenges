def equal_partition(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    half = total_sum // 2
    dp = [False] * (half + 1)
    dp[0] = True

    for num in arr:
        for i in range(half, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
            if(i == half):
                if(dp[i]):
                    return True

    return dp[half]

print(equal_partition([1, 5, 11, 5]))
# print(equal_partition([1, 3, 5]))
# print(equal_partition([1, 1, 1, 2, 3]))
