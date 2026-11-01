
from collections import deque


# Fixed capacities of the two jugs
JUG_A_CAPACITY = 4
JUG_B_CAPACITY = 3

# Target quantity to measure in Jug A
TARGET = 2


def get_next_states(state):
    """
    Generate all possible next states from the current state.

    A state is represented as (amount_in_A, amount_in_B).
    """

    a, b = state

    next_states = []

    # 1. Fill Jug A completely
    next_states.append(((JUG_A_CAPACITY, b), "Fill Jug A"))

    # 2. Fill Jug B completely
    next_states.append(((a, JUG_B_CAPACITY), "Fill Jug B"))

    # 3. Empty Jug A
    next_states.append(((0, b), "Empty Jug A"))

    # 4. Empty Jug B
    next_states.append(((a, 0), "Empty Jug B"))

    # 5. Pour water from Jug A into Jug B
    amount = min(a, JUG_B_CAPACITY - b)

    next_states.append(
        ((a - amount, b + amount), "Pour A -> B")
    )

    # 6. Pour water from Jug B into Jug A
    amount = min(b, JUG_A_CAPACITY - a)

    next_states.append(
        ((a + amount, b - amount), "Pour B -> A")
    )

    return next_states


def bfs_water_jug():
    """
    Use Breadth-First Search to find the shortest
    sequence of states that reaches the target.
    """

    initial_state = (0, 0)

    # Queue stores states waiting to be explored
    queue = deque([initial_state])

    # Set of states already explored or discovered
    visited = {initial_state}

    # Store the parent state and operation for each state
    parent = {
        initial_state: (None, None)
    }

    while queue:

        # Remove the oldest state from the queue
        current_state = queue.popleft()

        a, b = current_state

        # Check whether Jug A contains the target
        if a == TARGET:

            # Reconstruct the solution path
            path = []
            state = current_state

            while state is not None:

                previous_state, action = parent[state]

                path.append((state, action))

                state = previous_state

            # Reverse to obtain initial-to-goal order
            path.reverse()

            return path

        # Generate all possible next states
        for next_state, action in get_next_states(current_state):

            # Avoid exploring the same state repeatedly
            if next_state not in visited:

                visited.add(next_state)

                # Save how this state was reached
                parent[next_state] = (
                    current_state,
                    action
                )

                # Add the new state to the queue
                queue.append(next_state)

    # Return None if no solution exists
    return None


def display_solution(path):

    if path is None:
        print("No solution exists.")
        return

    print("\nWATER JUG PROBLEM SOLUTION")
    print("-" * 40)

    print("Jug A Capacity:", JUG_A_CAPACITY, "liters")
    print("Jug B Capacity:", JUG_B_CAPACITY, "liters")
    print("Target:", TARGET, "liters")

    print("\nSequence of State Transitions:")
    print("-" * 40)

    # Display initial state
    print("Step 0: Start ->", path[0][0])

    # Display each transition
    for step in range(1, len(path)):

        state, action = path[step]

        print(
            f"Step {step}: {action} -> {state}"
        )

    print("\nGoal State Reached:", path[-1][0])


# Main program
solution = bfs_water_jug()

display_solution(solution)
