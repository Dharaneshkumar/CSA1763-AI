from queue import PriorityQueue

def a_star(graph, heuristic, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {start: None}
    g_score = {start: 0}

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_list.put((f_score, neighbor))
                came_from[neighbor] = current

    return None

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 6},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 1},
    'E': {'B': 6, 'F': 2},
    'F': {'C': 5, 'E': 2}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 0
}

start_node = 'A'
goal_node = 'F'
result = a_star(graph, heuristic, start_node, goal_node)
print("Path found:", result)
