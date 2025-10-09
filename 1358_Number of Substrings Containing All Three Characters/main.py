class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        res= 0
        cnt = defaultdict(int)
        for r, c in enumerate(s):
            cnt[c]+=1
            while len(cnt) == 3:
                out = s[l]
                cnt[out]-=1
                if cnt[out] == 0:
                    del cnt[out]
                l+=1
            res += l
        return res
