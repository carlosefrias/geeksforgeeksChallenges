# Given an encoded string s, the task is to decode it. The encoding rule is :

# k[encodedString], where the encodedString inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets.
# Note: The test cases are generated so that the length of the output string will never exceed 105 .

# Examples:

# Input: s = "1[b]"
# Output: "b"
# Explanation: "b" is present only one time.
# Input: s = "3[b2[ca]]"
# Output: "bcacabcacabcaca"
# Explanation:
# 1. Inner substring “2[ca]” breakdown into “caca”.
# 2. Now, new string becomes “3[bcaca]”
# 3. Similarly “3[bcaca]” becomes “bcacabcacabcaca ” which is final result.


def decode(s):
    stack = []
    stack.append(["", 1])
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch.isalpha():
            stack[-1][0] += ch
        elif ch == "[":
            stack.append(["", int(num)])
            num = ""
        else:
            st, k = stack.pop()
            stack[-1][0] += st * k
    return stack[0][0]

print(decode("3[b2[ca]]")) # bcacabcacabcaca
print(decode("1[b]")) # b 
print(decode("2[ab]")) # abab
print(decode("2[a2[b]c]")) # abbcabbc
print(decode("2[a2[b]c]3[d]")) # abbcabbcddd
print(decode("2[a2[b]c]3[d]4[e]")) # abbcabbcdddeee