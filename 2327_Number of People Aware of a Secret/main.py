class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 1_000_000_007
        # known[i] 表示恰好在第 i 天得知秘密的人数
        known = [0] * (n + 1)
        known[1] = 1

        for i in range(1, n + 1):
            known[i] %= MOD
            # 恰好在第 i 天得知秘密的人，会在第 [i+delay, i+forget-1] 天分享秘密
            for j in range(i + delay, min(i + forget, n + 1)):
                known[j] += known[i]

        # 统计在第 n 天没有忘记秘密的人数
        # 这要求 i+forget-1 >= n，解得 i >= n-forget+1
        return sum(known[-forget:]) % MOD


# n=6 delay=2 forget=4
# n=4 delay=1 forget=3


