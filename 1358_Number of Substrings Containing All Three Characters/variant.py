from collections import defaultdict

# 【第二题】
# 输入：
# 一个仅由小写英文字母组成的字符串 s。
# 目标：
# 计算字符串 s 中有多少个子串同时满足以下两个条件：
# 该子串只包含元音字母（a, e, i, o, u）。
# 该子串中，五个元音字母 a, e, i, o, u 必须全部都出现至少一次。和LeetCode 1358 类似。


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


'''
TODO
s = "aaeiiiouuuuuuuxawaeiouhaaaaaaeiou"
找到 s 中所有符合条件的子串

NOTE
s => ["aaeiiiouuuuuuu", "a", "aeiou", "aaaaaaeiou"]
         s    f          X      1           s   f     => return 21
        这里 r 在每个 u 都会 + 2
ans += left
内层循环结束时，右端点固定在 right, 左端点在 0, 1, 2, ..., left - 1, 一共有 left 个

'''
def countVowelSubstrings2(s: str) -> int:
    # parse vowels substrs
    vowel_strs = []
    vowels = 'aeiou'
    pivot = res = 0
    for i, c in enumerate(s):
        if c not in vowels:
            vowel_strs.append(s[pivot: i])
            pivot = i + 1
    vowel_strs.append(s[pivot:])

    # calculate with sliding window
    for v_s in vowel_strs:
        if len(v_s) < 5:
            continue
        slow = 0
        window = defaultdict(int)
        for fast, curr in enumerate(v_s):
            window[curr] += 1
            while len(window) >= 5:
                window[v_s[slow]] -= 1
                if not window[v_s[slow]]:
                    del window[v_s[slow]]
                slow += 1
            res += slow
    return res


s = "aaeiiiouuuuuuuxawaeiouhaaaaaaeiou"
print(countVowelSubstrings2(s))  # 21

s = "aaeiouxa"
print(countVowelSubstrings2(s))  # 2

s = "aaeiouxaaeiou"
print(countVowelSubstrings2(s))  # 4


'''
TODO
s = "aaeiiiouuuuuuuxawaeiouhaaaaaaeiou"
找到 s 中所有符合条件的子串

NOTE
s => ["aaeiiiouuuuuuu", "a", "aeiou", "aaaaaaeiou"]
        l     r          X      1           l   r     => return 21
       2 * 7 = 14                       6 * 1 = 6
找最短的，包含所有元音的子串，然后计算左右两边有多少 vowels, 相乘即为结果

'''
def countVowelSubstrings3(s: str) -> int:
    # parse vowels substrs
    vowel_strs = []
    vowels = 'aeiou'
    pivot = res = 0
    for i, c in enumerate(s):
        if c not in vowels:
            vowel_strs.append(s[pivot: i])
            pivot = i + 1
    vowel_strs.append(s[pivot:])

    # calculate with sliding window
    for v_s in vowel_strs:
        if len(v_s) < 5:
            continue
        l, r = 0, len(v_s) - 1
        slow = 0
        window = defaultdict(int)
        min_len = len(v_s)
        for fast, curr in enumerate(v_s):
            window[curr] += 1
            while slow <= fast and len(window) >= 5:
                if fast - slow + 1 < min_len:
                    min_len = fast - slow + 1
                    l, r = slow, fast
                window[v_s[slow]] -= 1
                if not window[v_s[slow]]:
                    del window[v_s[slow]]
                slow += 1
        l_cpt, r_cpt = l + 1, len(v_s) - r
        res += l_cpt * r_cpt
    return res


s = "aaeiiiouuuuuuuxawaeiouhaaaaaaeiou"
print(countVowelSubstrings3(s))  # 21

s = "aaeiouxa"
print(countVowelSubstrings3(s))  # 2

s = "aaeiouxaaeiou"
print(countVowelSubstrings3(s))  # 4
