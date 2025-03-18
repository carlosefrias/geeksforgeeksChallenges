def is_subset_sum(arr, target):
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
            if(i == target):
                if(dp[i]):
                    return True

    return dp[target]

print(is_subset_sum([3, 34, 4, 12, 5, 2], 9))
print(is_subset_sum([3, 34, 4, 12, 5, 2], 30))
print(is_subset_sum([1, 2, 3], 6))
