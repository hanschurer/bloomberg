# https://www.1point3acres.com/bbs/thread-1123547-1-1.html


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        
        for c in set(s):
            if s.count(c)<k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        
        return n
        