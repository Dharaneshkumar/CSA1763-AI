from collections import deque
initial_state = (3, 3, 1)  
goal_state = (0, 0, 0)     
def is_valid(state):
    """ Check if a state is valid. """
    missionaries, cannibals, _ = state
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if (missionaries > 0 and missionaries < cannibals): 
        return False
    if (3 - missionaries > 0 and 3 - missionaries < 3 - cannibals):  
        return False
    return True
def get_successors(state):
    """ Generate all possible valid successors from the current state. """
    successors = []
    missionaries, cannibals, boat = state
    if boat == 1:  
        moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]  
    else:  
        moves = [(-1, 0), (0, -1), (-2, 0), (0, -2), (-1, -1)]  
    for m, c in moves:
        new_state = (missionaries - m, cannibals - c, 1 - boat)  
        if is_valid(new_state):
            successors.append(new_state)
    return successors
def bfs(initial_state, goal_state):
    """ Perform BFS to find the solution. """
    queue = deque([(initial_state, [])])  
    visited = set()  
    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state == goal_state:
            return path + [current_state]  
        
        for successor in get_successors(current_state):
            queue.append((successor, path + [current_state]))
    return None  
def print_solution(solution):
    """ Print the solution steps. """
    if solution:
        for i, step in enumerate(solution):
            print(f"Step {i}: Missionaries on left: {step[0]}, Cannibals on left: {step[1]}, Boat on {'left' if step[2] == 1 else 'right'} side")
    else:
        print("No solution found.")
solution = bfs(initial_state, goal_state)
print_solution(solution)
