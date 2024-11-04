from itertools import permutations

def travelling_salesman(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    for perm in permutations(vertices):
        current_path_weight = 0
        k = start
        for j in perm:
            current_path_weight += graph[k][j]
            k = j
        current_path_weight += graph[k][start]
        min_path = min(min_path, current_path_weight)
    return min_path

graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

start_node = 'A'
result = travelling_salesman(graph, start_node)
print("Minimum cost of the TSP:", result)
