# Write a function to crush candy in one dimensional board. In candy crushing games, groups of like items are removed from the board. In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. This process should be repeated as many time as possible. You should greedily remove characters from left to right.


# Input: "aaabbbc"
# Output: "c"
# Explanation:
# 1. Remove 3 'a': "aaabbbbc" => "bbbbc"
# 2. Remove 4 'b': "bbbbc" => "c"

# Input: "aabbbacd"
# Output: "cd"
# Explanation:
# 1. Remove 3 'b': "aabbbacd" => "aaacd"
# 2. Remove 3 'a': "aaacd" => "cd"

# Input: "aabbccddeeedcba"
# Output: ""
# Explanation:
# 1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
# 2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
# 3. Remove 3 'c': "aabbcccba" => "aabbba"
# 4. Remove 3 'b': "aabbba" => "aaa"
# 5. Remove 3 'a': "aaa" => ""

# Input: "aaabbbacd"
# Output: "acd"
# Explanation:
# 1. Remove 3 'a': "aaabbbacd" => "bbbacd"
# 2. Remove 3 'b': "bbbacd" => "acd"

# Follow-up:
# What if you need to find the shortest string after removal?

# Input: "aaabbbacd"
# Output: "cd"
# Explanation:
# 1. Remove 3 'b': "aaabbbacd" => "aaaacd"
# 2. Remove 4 'a': "aaaacd" => "cd"

def candy_crush(s, k):
    stack = []
    for i in range(len(s)):
        if stack and stack[-1][0]==s[i]:
            stack[-1][1] += 1
        else:
            if stack and stack[-1][1]>=k:
                stack.pop()
            if stack and stack[-1][0]==s[i]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])
    if stack and stack[-1][1]>=k:
        stack.pop()
    return ''.join(char*freq for char, freq in stack)



print(candy_crush("abbbcc",3)) # c
print(candy_crush("aaaabbbc",3)) # c
print(candy_crush("aabbbacd",3)) # cd
print(candy_crush("aabbccddeeedcba",3)) # blank expected
print(candy_crush("aabbbaacd",3)) # cd
print(candy_crush("dddabbbbaccccaax",3)) # x