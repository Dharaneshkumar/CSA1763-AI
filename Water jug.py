from collections import deque
def water_jug_bfs(capacity1, capacity2, target):
    queue = deque()
    visited = set()
    queue.append((0, 0))
    while queue:
        jug1, jug2 = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        if jug1 == target or jug2 == target:
            return True
        queue.append((capacity1, jug2))
        queue.append((jug1, capacity2))
        queue.append((0, jug2))
        queue.append((jug1, 0))
        pour_to_jug2 = min(jug1, capacity2 - jug2)
        queue.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        pour_to_jug1 = min(jug2, capacity1 - jug1)
        queue.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
    return False
def water_jug_problem(capacity1, capacity2, target):
    if target > max(capacity1, capacity2):
        return "Not possible to measure the target."
    if water_jug_bfs(capacity1, capacity2, target):
        return f"It is possible to measure exactly {target} liters."
    else:
        return f"It is not possible to measure exactly {target} liters."
jug1_capacity = 4  
jug2_capacity = 3  
target_amount = 2  
result = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
print(result)
