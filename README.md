# Water Jug Problem Using BFS

## Overview

This project implements the classic Water Jug Problem using Breadth-First Search (BFS), a state-space search algorithm.

The objective is to measure exactly 2 liters of water using two jugs with fixed capacities.

## Problem Configuration

- Jug A Capacity: 4 liters
- Jug B Capacity: 3 liters
- Target Quantity: 2 liters
- Initial State: (0, 0)
- Goal Condition: Jug A contains exactly 2 liters

## State Representation

Each state is represented as a tuple `(A, B)`.

- A represents the amount of water in Jug A.
- B represents the amount of water in Jug B.

## Allowed Operations

1. Fill Jug A
2. Fill Jug B
3. Empty Jug A
4. Empty Jug B
5. Pour water from Jug A into Jug B
6. Pour water from Jug B into Jug A

## Algorithm

Breadth-First Search (BFS) is used to explore the state space.

The implementation uses:

- A queue to explore states level by level.
- A visited set to prevent repeated exploration.
- A parent dictionary to store previous states and operations.
- Path reconstruction to display the exact sequence of transitions.

## Solution Path

The solution found by BFS is:

`(0,0) → (0,3) → (3,0) → (3,3) → (4,2) → (0,2) → (2,0)`

The goal state is `(2,0)`.

## How to Run

Make sure Python 3 is installed.

Run the following command:

```bash
python water_jug_problem.py
```

## Conclusion

The Water Jug Problem is successfully solved using BFS. The program finds a shortest sequence of operations that reaches the target quantity and displays the complete state transition path.
