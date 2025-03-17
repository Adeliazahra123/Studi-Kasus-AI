from collections import deque
import heapq

# State Representation: (farmer, wolf, sheep, cabbage)
initial_state = (0, 0, 0, 0)  # 0: left side, 1: right side
goal_state = (1, 1, 1, 1)

# Valid moves: (farmer moves alone or with one item)
moves = [(1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1)]

# Constraints: No wolf-sheep alone, no sheep-cabbage alone
def is_valid(state):
    farmer, wolf, sheep, cabbage = state
    if (wolf == sheep and farmer != wolf) or (sheep == cabbage and farmer != sheep):
        return False
    return True

# Generate next valid states
def get_neighbors(state):
    neighbors = []
    for move in moves:
        new_state = tuple(state[i] ^ move[i] for i in range(4))
        if is_valid(new_state):
            neighbors.append(new_state)
    return neighbors

# BFS Implementation
def bfs():
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))
    return None

# DFS Implementation
def dfs():
    stack = [(initial_state, [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == goal_state:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            stack.append((neighbor, path + [state]))
    return None

# UCS Implementation
def ucs():
    pq = [(0, initial_state, [])]  # (cost, state, path)
    visited = set()
    while pq:
        cost, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (cost + 1, neighbor, path + [state]))
    return None

# Run and print results
print("BFS Solution:")
print(bfs())
print("\nDFS Solution:")
print(dfs())
print("\nUCS Solution:")
print(ucs())
