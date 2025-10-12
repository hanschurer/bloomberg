class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        l = 0
        maxf = 0       # historical max frequency in the current expansion
        best = 0

        for r, ch in enumerate(s):
            count[ch] += 1
            # only ever increase maxf
            if count[ch] > maxf:
                maxf = count[ch]

            '''
            If replacements needed exceed k, shrink from the left.  A window is valid if 
                window_length - max_freq_in_window ≤ k
            instead of recomputing max_freq_in_window (or shrinking it) when you move l, just keep a historical maxf = the largest frequency seen while expanding r. 
            We only increase maxf as counts grow, never decrease it when shrinking. Even if maxf is not accurate in the shrinked window,
            the algorithm remains correct: it might allow some windows that are technically invalid, but that only causes extra shrinking later and never inflates the final answer.

            We only ever record best = max(best, window_size) at times when the condition (r - l + 1) - maxf ≤ k holds with our (possibly outdated) maxf.

            情况 A：当继续扩张（r 右移）时，(r-l+1) - maxf 只会更大，更容易触发 while (r-l+1) - maxf > k强制shrink:
                于是窗口会被强制缩小到再次满足条件为止。这个过程不会把 best 再“抬得更高”，因此不会产生比真实可行长度更大的答案。
            情况 B：过期的 maxf 很快会被“兑现”
                随着 r 继续右移，某个字符的计数会增加，真实最大频次 true_maxf 迟早会追上或超过我们保存的 maxf。
                一旦 true_maxf ≥ maxf，先前那个长度 L（甚至更长）会在某个时刻真正变成合法窗口（满足 L - true_maxf ≤ k）。
                所以，即便我们在“看起来合法”的瞬间记录了 L，这个 L 实际上在后续某个时刻确实可达，不会虚高。
            '''
            
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best

# tc: O(n): We access each index of the string at most two time: when it is added to the sliding window, and when it is removed from the sliding window. 
#   The sliding window always moves forward. In each step, we update the frequency map, maxFrequency, and check for validity, they are all constant-time operations. 

# sc: O(m): this approach requires an auxiliary frequency map. The maximum number of keys in the map equals the number of unique characters in the string. 
#    If there are m unique characters (m<=26 unique English characters), then the memory required is proportional to m.