def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    jumps = [float('inf')] * n
    jumps[0] = 0

    for i in range(1, n):
        for j in range(i):
            if i <= j + arr[j] and jumps[j] != float('inf'):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break

    return jumps[-1] if jumps[-1] != float('inf') else -1

print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(min_jumps([1, 4, 3, 2, 6, 7]))
print(min_jumps([0, 10, 20]))
print(min_jumps([0]))
print(min_jumps([]))
