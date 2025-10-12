# https://www.1point3acres.com/bbs/thread-963278-1-1.html
# candy crush 的原题


# — Title: Clean Canceling Trade Pairs in Log II
# Difficulty: Medium
# Prompt: Given a trade action string, repeatedly remove groups of k adjacent identical characters (e.g., k identical “B” = buy corrections) until no more removals are possible. Return the final string (the cleaned trade log).

class Solution:
    '''
    NOTE
    1. remove duplicates on s
    2. 一遇到 k 个相同的字母就删掉（candy crush 是一直遍历 n 个相同字母再删，n >= k）
    3. 重复直到没有 k 个相同的字母

    SOLUTION
    deeedbbcccbdaa

    st = [[a, 2]]
    '''
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if not st or st[-1][0] != c:
                st.append([c, 1])
            else:
                st[-1][1] += 1
                if st and st[-1][1] >= k:
                    st.pop()
        return ''.join([c * cnt for c, cnt in st])
