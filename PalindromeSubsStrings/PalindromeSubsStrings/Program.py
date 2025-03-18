def count_ps(s):
    if len(s) < 2:
        return 0
    palindromes = []
    for length in range(2, len(s)):
        pos = 0
        while pos + length <= len(s):
            sub_string = s[pos:pos + length]
            if is_palindrome(sub_string):
                palindromes.append(sub_string)
            pos += 1

    return len(palindromes)

def is_palindrome(s):
    reverse = s[::-1]
    return s == reverse

# See https://aka.ms/new-console-template for more information

print(count_ps("abaab"))
print(count_ps("aaa"))
print(count_ps("abbaeae"))
