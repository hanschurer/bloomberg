# https://www.1point3acres.com/bbs/thread-1121985-1-1.html
from collections import defaultdict


# — Title: Longest Unique Client Session
# Difficulty: Medium
# Prompt: Given a session log string where each character represents a client token, return the length of the longest substring without repeating tokens, representing the longest continuous window of unique client activity.


# 标准解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = slow = 0
        window = defaultdict(int)
        for fast, curr in enumerate(s):
            window[curr] += 1
            while window[curr] > 1:
                window[s[slow]] -= 1
                slow += 1
            res = max(res, fast - slow + 1)
        return res

    '''
    s = "abcabcbb"
    slow = 1 => 'b'
    fast = 3 => 'a'
            res = 3 - 1 + 1 = 3 => 'bca'
    '''
    def lengthOfLongestSubstring_optimized(self, s: str) -> int:
        res = slow = 0
        last_occu = defaultdict(int)
        for fast, curr in enumerate(s):
            slow = max(slow, last_occu[curr])
            last_occu[curr] = fast + 1
            res = max(res, fast - slow + 1)
        return res

# Follow up: 如果要找所有長度最長的substring，多放了一個set去記錄左右端點，最後再用for loop 加回去



