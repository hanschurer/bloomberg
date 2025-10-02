# https://leetcode.com/problems/cheapest-flights-within-k-stops/editorial/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0

        for i in range(k+1):
            temp = costs[:]
            for u, v, price in flights:
                if costs[u] != float('inf'):
                    temp[v] = min(temp[v], costs[u] + price)
            costs = temp

        return -1 if costs[dst] == float('inf') else costs[dst]