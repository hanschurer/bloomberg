# 0, 1, …, n - 1 这 n 个数字排成一个圆圈，从数字 0 开始，每次从这个圆圈里删除第 m 个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
# 例如，n = 5，m = 3 时，依次删除的数字为 2、0、4、1，最后剩下的数字是 3。


# 五、注意：编号从 1 开始的情况
# 如果题目中人数编号是 1 ~ n（而非 0 ~ n-1），只需在最终结果上加 1 即可。例如：n=5, k=3，编号 1~5 时，最后存活者是 3 + 1 = 4（对应原编号 3→新编号 4）。


def lastRemaining(n: int, k: int) -> int:
    res = 0  # 初始条件：f(1) = 0
    # 从n=2推到n，因为f(n)依赖f(n-1)
    for i in range(2, n + 1):
        res = (res + k) % i
    return res

# 测试：n=5, k=3 → 输出3
print(lastRemaining(5, 3))  # 结果：3



def lastRemaining(n: int, k: int) -> int:
    if n == 1:
        return 0
    # 先求n-1的结果，再映射到n的结果
    return (lastRemaining(n - 1, k) + k) % n

print(lastRemaining(5, 3))  # 结果：3