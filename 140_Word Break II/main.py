"""
原題。
"""
from typing import List


# 暴力解法
def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    word_set = set(wordDict)

    def dfs(idx: int) -> None:
        if curr and curr[-1] not in word_set:
            return
        if idx == len(s):
            res.append(' '.join(curr))
            return
        for i in range(idx + 1, len(s) + 1):
            word = s[idx: i]
            curr.append(word)
            dfs(i)
            curr.pop()

    res, curr = [], []
    dfs(0)
    return res

# 优化思路
def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    memo = {}

    def dfs(s: str) -> None:
        if s in memo:
            return memo[s]
        res = []
        for word in wordDict:
            if s.startswith(word):
                if s == word:
                    res.append(word)
                else:
                    for n_s in dfs(s[len(word):]):
                        res.append(f"{word} {n_s}")
        memo[s] = res
        return res

    return dfs(s)
