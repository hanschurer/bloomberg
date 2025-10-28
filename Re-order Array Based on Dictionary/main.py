# https://www.1point3acres.com/bbs/thread-1120131-1-1.html

# simiar to leetcode 332
# Consider a vector of employees with a name and their title:
# [<John, Manager>, <Sally, CTO>, <Sam, CEO>, <Drax, Engineer>, <Bob, CFO>, <Daniel, Engineer>]

# And a dictionary where the keys report to the values:
# {[CTO, CEO], [Manager, CTO], [Engineer, Manager], [CFO, CEO]}

# Re-order the vector of employees according to the dictionary mappings. The vector of employees can be extremely big, however the dictionary only contains the title orderings.

# Sample output:
# [<Drax, Engineer>, <Daniel, Engineer>, <John, Manager>, <Sally, CTO>, <Bob, CFO>, <Sam, CEO>]

# Note that in this case, CTO and CFO both report to CEO so they are both before CEO and above the next biggest thing, which is manager. They can also be in either order in this case.

from collections import defaultdict, deque
from typing import Dict, List, Tuple, Any


def solution(employees: List[Tuple[str, str]], reports: Dict[str, Any]) -> List[Tuple[str, str]]:
    # find ordering based on reports w/ topo sort
    ind = {}
    graph = defaultdict(list)
    for k, v in reports.items():
        graph[v].append(k)
        ind.setdefault(k, 0)
        ind.setdefault(v, 0)
        ind[k] += 1

    # find ordering from CEO, reverse the order
    orders = {}
    order = len(ind)
    q = deque(title for title, indegree in ind.items() if not indegree)
    while q:
        for _ in range(len(q)):
            cur_title = q.popleft()
            orders[cur_title] = order
            for n_title in graph[cur_title]:
                ind[n_title] -= 1
                if not ind[n_title]:
                    q.append(n_title)
        order -= 1

    return sorted(employees, key=lambda x: (orders[x[1]]))


employees = [
    ("John", "Manager"),
    ("Sally", "CTO"),
    ("Sam", "CEO"),
    ("Drax", "Engineer"),
    ("Bob", "CFO"),
    ("Daniel", "Engineer")
]        
reports = {
    "CTO": "CEO",
    "Manager": "CTO",
    "Engineer": "Manager",
    "CFO": "CEO"
}
print(solution(employees, reports))

