'''
source: https://www.1point3acres.com/bbs/thread-1148521-1-1.html

'''
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)