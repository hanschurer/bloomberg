'''
**Collatz Conjecture is** the number of steps needed to transform x into 1 using the following steps:

- if x is even then x = x / 2
- if x is odd then x = 3 * x + 1

Iterative approach which implements backtracking as a means to memorize intermediate numbers
'''
from typing import Optional, List

# 必须是 Iterative approach!!!
class CollatzConjecture:

    def __init__(self):
        self.memos = {}

    def count_steps(self, val: int) -> int:
        prev, steps = [], 0
        while val > 1:
            if val in self.memos:
                steps += self.memos[val]
                break
            prev.append(val)
            if val % 2 == 0:
                val //= 2
            else:
                val = 3 * val + 1
            steps += 1

        for i in range(len(prev) - 1, -1, -1):
            self.memos[prev[i]] = steps - i
        return steps


# Recursive, 仅供参考
class CollatzConjecture2:

    def __init__(self):
        self.memos = {1: 0}

    def count_steps(self, val: int) -> int:
        if val in self.memos:
            return self.memos[val]
        count = self.count_steps(val // 2 if val % 2 == 0 else 3 * val + 1) + 1
        self.memos[val] = count
        return count
