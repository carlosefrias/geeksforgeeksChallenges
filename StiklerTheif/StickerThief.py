def find_max_sum(arr):
    n = len(arr)
    dp = [0]*(n)
    if(n==0):
        return 0
    if(n==1):
        return arr[0]
    if(n==2):
        return max(arr[0], arr[1])
        
    dp[0] = arr[0]
    for i in range(1,n):
        dp[i] = arr[i] + max(dp[i-2], dp[i-3])
    return max(dp[n-1], dp[n-2])

print(find_max_sum([768, 398]))
print(find_max_sum([9, 10, 5, 7]))
print(find_max_sum([6, 5, 5, 7, 4]))
print(find_max_sum([1, 5, 3]))
print(find_max_sum([4, 4, 4, 4]))