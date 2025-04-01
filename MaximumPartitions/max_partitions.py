# Given a string s of lowercase English alphabets, your task is to return the maximum number of substrings formed, 
# after possible partitions (probably zero) of s such that no two substrings have a common character.

def max_partitions(s):
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    partitions = 0
    current_end = 0
    for i, char in enumerate(s):
        current_end = max(current_end, last_occurrence[char])
        if i == current_end:
            partitions += 1

    return partitions

print(max_partitions("acbbcc"))  # Output: 2
print(max_partitions("ababcbacadefegdehijhklij"))  # Output: 3
print(max_partitions("aaa"))  # Output: 1

# Examples:

# Input: s = "acbbcc"
# Output: 2
# Explanation: "a" and "cbbcc" are two substrings that do not share any characters between them.
# Input: s = "ababcbacadefegdehijhklij"
# Output: 3
# Explanation: Partitioning at the index 8 and at 15 produces three substrings: “ababcbaca”, “defegde”, and “hijhklij” such that none of them have a common character. So, the maximum number of substrings formed is 3.
# Input: s = "aaa"
# Output: 1
# Explanation: Since the string consists of same characters, no further partition can be performed. Hence, the number of substring (here the whole string is considered as the substring) is 1.
# Constraints:
# 1 ≤ s.size() ≤ 105
# 'a' ≤ s[i] ≤ 'z'