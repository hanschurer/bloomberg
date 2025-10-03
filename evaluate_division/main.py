# Array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 US is equal to 0.77 GBP an array containing a 'from' currency and a 'to' currency. Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency. Your return value should be a number
from collections import defaultdict
from typing import List


# Example:
# You are given the following parameters:
# Rates: ['USD', 'JPY', 110] ['USD', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
# To/From currency: ['GBP', 'AUD']
# Output: 1.89

def evaluate_division(rates: List[List[str]], to_from: List[str]) -> float:
    graph = defaultdict(list)
    for src, des, rate in rates:
        graph[src].append((des, rate))
        graph[des].append((src, 1 / rate))

    def dfs(currency: str, conversion: float) -> None:
        nonlocal ans

        visited.add(currency)
        if currency == to_from[1]:
            ans = conversion
            return
        for neighbor, rate in graph[currency]:
            if neighbor not in visited:
                dfs(neighbor, conversion * rate)
                if ans != float('-inf'):
                    return

    ans = -1
    visited = set()
    dfs(to_from[0], 1.0)
    return ans

rates = [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]]
to_from= ['GBP', 'AUD']
print(f"{evaluate_division(rates, to_from):.2f}")  # 1.88

rates = [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]]
to_from= ['GBP', 'EUR']
print(f"{evaluate_division(rates, to_from):.2f}")  # -1.0
