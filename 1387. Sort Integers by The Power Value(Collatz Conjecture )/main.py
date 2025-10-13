from functools import cache


# 这道题必须是 Iterative approach，不能是 Recursive approach，会被挂
@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def dfs(i: int) -> int:
    if i == 1:
        return 0
    if i % 2:
        return dfs((i * 3 + 1) // 2) + 2
    return dfs(i // 2) + 1

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # sorted 是稳定排序，我们只需比较 dfs 的返回值
        return sorted(range(lo, hi + 1), key=dfs)[k - 1]

