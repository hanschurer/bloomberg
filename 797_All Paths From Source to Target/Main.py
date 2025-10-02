'''
source: https://leetcode.com/discuss/post/7049289/bloomberg-sse-ny-phone-screen-full-loop-rpn92/
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths
from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e.,
there is a directed edge from node i to node graph[i][j]).
'''
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        backtracking
        '''
        ans = []

        n = len(graph)

        def backtracking(cur, path):
            nonlocal n
            path.append(cur)
            # leaf node or last node
            if not graph[cur] or cur == n - 1:
                if cur == n - 1:
                    ans.append(path[::])
                path.pop()
                return
            for nextVal in graph[cur]:
                backtracking(nextVal, path)
            path.pop()

        backtracking(0, [])

        return ans
def main():
    sol = Solution()

    # Test case 1
    graph1 = [[1, 2], [3], [3], []]
    expected1 = [[0, 1, 3], [0, 2, 3]]
    result1 = sol.allPathsSourceTarget(graph1)
    print("Test case 1:")
    print("Input:", graph1)
    print("Expected:", expected1)
    print("Got:", result1)
    print("Pass:", sorted(result1) == sorted(expected1))
    print()

    # Test case 2
    graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    expected2 = [
        [0, 4],
        [0, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 4]
    ]
    result2 = sol.allPathsSourceTarget(graph2)
    print("Test case 2:")
    print("Input:", graph2)
    print("Expected:", expected2)
    print("Got:", result2)
    print("Pass:", sorted(result2) == sorted(expected2))
    print()

    # Test case 3 (edge case: single node)
    graph3 = [[]]
    expected3 = [[0]]
    result3 = sol.allPathsSourceTarget(graph3)
    print("Test case 3:")
    print("Input:", graph3)
    print("Expected:", expected3)
    print("Got:", result3)
    print("Pass:", sorted(result3) == sorted(expected3))
    print()


if __name__ == "__main__":
    main()


