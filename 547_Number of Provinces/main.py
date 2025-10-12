'''

547. Number of Provinces
Solved
Medium
Topics
conpanies icon
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        union find
        '''
        n = len(isConnected)

        father = [0] * n
        # initialize the father array
        for i in range(n):
            father[i] = i

        def find(s):
            if s == father[s]:
                return s
            father[s] = find(father[s])

            return father[s]

        def join(f, s):
            f = find(f)
            s = find(s)
            if s == f:
                return

            father[s] = f

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    join(j, i)
        provinces = set()
        # compress the ancestor tree
        for i in range(n):
            provinces.add(find(i))
        return len(provinces)