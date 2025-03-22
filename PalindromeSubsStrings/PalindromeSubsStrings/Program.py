def count_ps(s):
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                count += 1
            else:
                break
            left -= 1
            right += 1
        return count

    n = len(s)
    count = 0
    for i in range(n):
        count += expand_around_center(i - 1, i + 1)
        count += expand_around_center(i, i + 1)

    return count


# See https://aka.ms/new-console-template for more information
print(count_ps("aba"))
print(count_ps("abaab"))
print(count_ps("aaa"))
print(count_ps("abbaeae"))
