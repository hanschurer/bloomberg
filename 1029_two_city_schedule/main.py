
# — Title: Assign Analysts to Two Cities (Cost Minimization)
# Difficulty: Medium
# Prompt: Each analyst must be sent to either City A or City B for a rotation. You’re given costs for each analyst to go to A and to B, and exactly half must go to each city. Minimize total travel cost and return that minimum.

def two_city_schedule(costs: List[list[int]])->int:

    costs = sorted(costs, key=lambda i: i[0] - i[1])

    n = len(costs)//2

    costa = sum(i for i,_ in costs[:n])
    costb = sum(i for _, i in costs[n:])

    return costa+costb