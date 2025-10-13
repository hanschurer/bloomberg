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

# 和面试官讨论后，所期望的解法：
def countInVowelBlock_lastPos(block: str) -> int:
    """
    使用“记录最新位置”的方法来计算。
    """
    total_count = 0
    n = len(block)
    last_pos = {'a': -1, 'e': -1, 'i': -1, 'o': -1, 'u': -1}
    
    for i in range(n):
        # 1. 更新当前字符的最新位置
        last_pos[block[i]] = i
        
        # 2. 找到五个元音最新位置中的最小值
        start_of_window = min(last_pos.values())
        
        # 3. 如果 start_of_window > -1，说明五个元音都出现过了
        if start_of_window > -1:
            # 4. 累加合法的子串数量
            total_count += (start_of_window + 1)
            
    return total_count

def is_vowel(char: str) -> bool:
    return char in 'aeiou'

def countVowelSubstrings_main(s: str) -> int:
    total_count = 0
    n = len(s)
    start = 0
    for i in range(n + 1):
        if i == n or not is_vowel(s[i]):
            vowel_block = s[start:i]
            if vowel_block:
                total_count += countInVowelBlock_lastPos(vowel_block)
            start = i + 1
    return total_count


# 双指针滑动窗口，使用 pivot 记录最后一个非元音字母的位置
def countVowelSubstrings2(s: str) -> int:
    window = defaultdict(int)
    res = slow = pivot = 0
    vowel_cnt = set()
    vowels = 'aeiou'

    for fast, curr in enumerate(s):
        window[curr] += 1
        if curr in vowels:
            vowel_cnt.add(curr)

        while slow <= fast and (
                len(vowel_cnt) >= 5 or (curr not in vowels and curr in window)):
            if window[s[slow]] == 1 and s[slow] in vowels:
                vowel_cnt.remove(s[slow])
            window[s[slow]] -= 1
            if not window[s[slow]]:
                del window[s[slow]]
            slow += 1
            if curr not in vowels:
                pivot = fast + 1
        res += slow - pivot
    return res

s = "aaeiouxa"
print(countVowelSubstrings2(s))  # 2

s2 = "aaeiouxaaeiou"
print(countVowelSubstrings2(s2)) # 4
