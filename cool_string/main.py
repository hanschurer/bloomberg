from collections import Counter

# Given a string,
# It can be cool string if
# 1. All Characters have same frequency
# 2. If we can remove only 1 character and make it a cool string


#  Create a function that returns true or false 
#  depending on whether the string passed in is 
#  valid or not.

#  A string is valid if all characters have an equal 
#  number of occurrences within it. 
#  You may also remove one character from the string 
#  to make it valid.

# Example:

# aaabbb -> true
# Explanation: Both a and b have same frequencies
# aaabbbcccc -> true
# Explanation: a and b occur 3 times but c occurs 4 times, we can remove 1 c to make this into a cool string
# aaabbbccccdddd -> false
# Explanation: a and b occur 3 times but c and d occur 4 times we'd have to remove 1 c and 1 d to make it cool string
# aabbcccdddeeee -> false
# Explanation: a and b occur 2 times, c and d occur 3 times, and e occurs 4 times. We'd have to remove 1 c and 2 e's to make it cool string

class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = sorted(Counter(word).values())  # 出现次数从小到大排序
        # 只有一种字符 or 去掉次数最少的 or 去掉次数最多的
        return len(cnt) == 1 or \
               cnt[0] == 1 and len(set(cnt[1:])) == 1 or \
               cnt[-1] == cnt[-2] + 1 and len(set(cnt[:-1])) == 1


# Test cases based on examples
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("aaabbb", True),
        ("aaabbbcccc", True), 
        ("aaabbbccccdddd", False),
        ("aabbcccdddeeee", False)
    ]
    
    print("Testing cool string examples:")
    print("=" * 40)
    
    for word, expected in test_cases:
        result = solution.equalFrequency(word)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{word}' -> {result} (expected: {expected})")
        
        # Show character frequencies for better understanding
        freq = Counter(word)
        print(f"   Frequencies: {dict(freq)}")
        print()