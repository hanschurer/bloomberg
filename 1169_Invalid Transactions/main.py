from collections import defaultdict
from typing import List

# variant: 输入已按照时间排序）
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
        for t in transactions:
            name, time, amount, city = t.split(',')
            trans[name][int(time)][city].append(int(amount))

        res = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            if int(amount) > 1000:
                res.append(t)
                continue
            s_t, e_t = int(time) - 60, int(time) + 61
            for cur_t in range(s_t, e_t):
                cities = trans[name][cur_t]
                if (cities and city not in cities) or (len(cities) > 1 and city in cities):
                    res.append(t)
                    break
        return res