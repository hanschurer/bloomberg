'''
source: 2025/10/9 first round VO

'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(t[i]) - ord('a')] -= 1
        res = 0
        for i in cnt:
            if i > 0:
                res += i
        return res
