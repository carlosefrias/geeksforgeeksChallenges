from functools import lru_cache

# You are given a string s and a list dictionary[] of words. Your task is to determine whether the string s can be formed by concatenating one or more words from the dictionary[].

# Note: From dictionary[], any word can be taken any number of times and in any order.

def work_break(s, dictionary):
    word_set = set(dictionary)  # Convert list to set for O(1) lookups

    @lru_cache(None)  # Cache results of recursive calls
    def can_break(start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and can_break(end):
                return True
        return False

    return can_break(0)


print(work_break("ilike", ["i", "like", "gfg"]))  # Output: True
print(work_break("ilikegfg", ["i", "like", "man", "india", "gfg"]))  # Output: True
print(work_break("i like gfg", ["i", "like", "man", "india", "gfg"]))  # Output: False



# Examples :

# Input: s = "ilike", dictionary[] = ["i", "like", "gfg"]
# Output: true
# Explanation: s can be breakdown as "i like".
# Input: s = "ilikegfg", dictionary[] = ["i", "like", "man", "india", "gfg"]
# Output: true
# Explanation: s can be breakdown as "i like gfg".
# Input: s = "ilikemangoes", dictionary[] = ["i", "like", "man", "india", "gfg"]
# Output: false
# Explanation: s cannot be formed using dictionary[] words.
# Constraints:
# 1 ≤ s.size() ≤ 3000
# 1 ≤ dictionary.size() ≤ 1000
# 1 ≤ dictionary[i].size() ≤ 100