def is_safe(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, color_list, node):
    if node == len(graph):
        return True
    
    for color in color_list:
        if is_safe(graph, colors, node, color):
            colors[node] = color
            if map_coloring(graph, colors, color_list, node + 1):
                return True
            colors[node] = None
    return False

def solve_map_coloring(graph, color_list):
    colors = [None] * len(graph)
    if map_coloring(graph, colors, color_list, 0):
        return colors
    else:
        return None

graph = [
    [1, 2],    
    [0, 2, 3], 
    [0, 1],    
    [1]        
]

color_list = ['Red', 'Green', 'Blue']
result = solve_map_coloring(graph, color_list)
print("Coloring Solution:", result)
