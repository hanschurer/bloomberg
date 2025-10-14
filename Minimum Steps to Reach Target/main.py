'''
source: https://www.1point3acres.com/bbs/thread-1023558-1-1.html
You start with the integer 1. At each step, you may perform exactly one of the following operations:
    n=n×2
    n=n÷3

Given a target integer t, determine the minimum number of steps required to reach t starting from 1.


# Example 1
Input: t = 2
Steps: 1 -> 2
Output: 1


# Example 2
Input: t = 10
One possible path: 1 -> 2 -> 4 -> 8 -> 16 -> 5 -> 10
Steps = 6
Output: 6

# Example 3
Input: t = 1
Already at target
Output: 0
'''
import collections


def min_steps_to_target(t: int) -> int:
    """
    Calculates the minimum number of operations to reach the target integer t from 1.
    Available operations are: n = n * 2 or n = n // 3.

    Args:
        t: The target positive integer.

    Returns:
        The minimum number of steps to reach t.
    """
    if t <= 0:
        return -1  # Invalid input, the problem implies t is a positive integer
    if t == 1:
        return 0

    # Use a deque for Breadth-First Search (BFS)
    # The queue stores tuples of (current_number, steps)
    queue = collections.deque([(1, 0)])

    # Use a set to keep track of visited numbers to avoid redundant computations
    visited = {1}

    while queue:
        current_num, steps = queue.popleft()

        # Direction 1: n = n * 2
        next_num_mul = current_num * 2
        if next_num_mul == t:
            return steps + 1
        if next_num_mul not in visited:
            visited.add(next_num_mul)
            queue.append((next_num_mul, steps + 1))

        # Direction 2: n = n // 3
        next_num_div = current_num // 3
        if next_num_div > 0:
            if next_num_div == t:
                return steps + 1
            if next_num_div not in visited:
                visited.add(next_num_div)
                queue.append((next_num_div, steps + 1))

    return -1  # Should not be reached for any positive integer t


# --- Automated Test Script ---
def run_tests():
    """
    Runs a predefined set of test cases to verify the algorithm's correctness.
    """
    test_cases = [
        {"id": 1, "input": 1, "expected": 0, "description": "Example 3: Target is 1"},
        {"id": 2, "input": 2, "expected": 1, "description": "Example 1: 1 -> 2"},
        {"id": 3, "input": 10, "expected": 6, "description": "Example 2: 1 -> ... -> 10"},
        {"id": 4, "input": 3, "expected": 7, "description": "Path requires multiplication then division"},
        {"id": 5, "input": 6, "expected": 8, "description": "A more complex path"},
        {"id": 7, "input": 20, "expected": 7, "description": "A relatively direct path"},
    ]

    print("--- Starting Automated Tests ---")
    passed_count = 0

    for test in test_cases:
        case_id = test["id"]
        t_input = test["input"]
        expected = test["expected"]
        desc = test["description"]

        print(f"\n[Test Case #{case_id}: {desc}]")
        print(f"  Input: t = {t_input}")
        print(f"  Expected Output: {expected}")

        actual = min_steps_to_target(t_input)

        print(f"  Actual Output:   {actual}")

        if actual == expected:
            print("  Result: \033[92mPASSED\033[0m")  # Green text for PASSED
            passed_count += 1
        else:
            print(f"  Result: \033[91mFAILED\033[0m")  # Red text for FAILED

    print("\n--- Test Summary ---")
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {len(test_cases) - passed_count}")
    print("--------------------")


if __name__ == "__main__":
    # Running this script will display the results for all test cases.
    run_tests()
