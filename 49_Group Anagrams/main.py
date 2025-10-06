'''
source: https://www.1point3acres.com/bbs/thread-1148693-1-1.html
follow up -> 就是如果字符串包含的字符不只是英文字母，还包含很多很多其他ascii的字符，该怎么优化。
'''
from typing import List

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    # follow up
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 256
            for ch in word:
                freq[ord(ch)] += 1
            groups[tuple(freq)].append(word)
        print(groups)
        return list(groups.values())

def test_group_anagrams():
    sol = Solution()

    assert sorted([sorted(g) for g in sol.groupAnagrams2(["eat","tea","tan","ate","nat","bat"])]) == \
           sorted([["bat"], ["nat","tan"], ["ate","eat","tea"]])

    assert sorted([sorted(g) for g in sol.groupAnagrams2(["123","231","312","456"])]) == \
           sorted([["123","231","312"], ["456"]])

    assert sorted([sorted(g) for g in sol.groupAnagrams2(["!@#","@#!","abc","cab"])]) == \
           sorted([["!@#","@#!"], ["abc","cab"]])


    assert sorted([sorted(g) for g in sol.groupAnagrams2(["","", "a","A"])]) == \
           sorted([["",""], ["a"], ["A"]])

    print("All tests passed!")