# Follow up: 找到符合条件的所有pairs
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        m, ans = inf, []
        for a, b in pairwise(sorted(arr)):
            if (cur := b - a) < m:
                m, ans = cur, [[a, b]]
            elif cur == m:
                ans.append([a, b])
        return ans
