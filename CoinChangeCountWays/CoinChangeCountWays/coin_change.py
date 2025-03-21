# def dfs_recursive(coins, target, current, ways, memo):
#     current_sum = sum(current)
#     if current_sum == target:
#         current.sort()
#         str_repr = f"[{','.join(map(str, current))}]"
#         if str_repr not in ways:
#             ways.add(str_repr)
#         return
#     if current_sum in memo:
#         return
#     memo.add(current_sum)
#     for coin in coins:
#         next_combination = current + [coin]
#         if sum(next_combination) <= target:
#             dfs_recursive(coins, target, next_combination, ways, memo)

# def count_coin_change(coins, target):
#     if target == 0:
#         return 0
#     if target < min(coins):
#         return 0
#     ways = set()
#     memo = set()
#     dfs_recursive(coins, target, [], ways, memo)
#     return len(ways)




def add(arr):
    res = 0
    for i in arr:
        res += i
    return res

def dfs_recursive(coins, sum, current, ways, memo):
    current_sum = add(current)
    if current_sum == sum:
        current.sort()
        str_repr = f"[{','.join(map(str, current))}]"
        if str_repr not in ways:
            ways.add(str_repr)
        return
    if current_sum in memo:
        return
    memo.add(current_sum)
    for coin in coins:
        next_combination = current + [coin]
        if add(current) + coin <= sum:
            dfs_recursive(coins, sum, next_combination, ways, memo)

def count_coin_change(coins, sum):
    if sum == 0:
        return 0
    if sum < min(coins):
        return 0
    ways = set()
    memo = set()
    dfs_recursive(coins, sum, [], ways, memo)
    return len(ways) 

print(count_coin_change([1, 2, 3], 4)) # 4
print(count_coin_change([2, 5, 3, 6], 10)) # 5
print(count_coin_change([5, 10], 3)) # 0
print(count_coin_change([1, 2, 3], 5)) # 5
print(count_coin_change([1, 2, 3], 6)) # 7
print(count_coin_change([1, 2, 3], 7)) # 8