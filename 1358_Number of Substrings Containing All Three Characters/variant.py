from collections import defaultdict



# 【第二题】
# 输入：
# 一个仅由小写英文字母组成的字符串 s。
# 目标：
# 计算字符串 s 中有多少个子串同时满足以下两个条件：
# 该子串只包含元音字母（a, e, i, o, u）。
# 该子串中，五个元音字母 a, e, i, o, u 必须全部都出现至少一次。和LeetCode 1358 类似。

class Solution:
    def countVowelSubstrings(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        res = 0
        cnt = defaultdict(int)
        
        for r, c in enumerate(s):
            # 只处理元音字母
            if c not in vowels:
                # 遇到非元音，重置窗口
                cnt.clear()
                l = r + 1
                continue
            
            cnt[c] += 1
            
            # 当窗口包含所有5个元音时，尝试收缩左边界
            while len(cnt) == 5:
                # 记录当前左边界位置，用于计算有效子串数量
                current_left = l
                
                # 移动左指针，直到不再包含所有5个元音
                out = s[l]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                l += 1
                
                # 从current_left到l-1的每个位置作为左边界，都能形成有效的子串
                res += len(s) - r
        
        return res
