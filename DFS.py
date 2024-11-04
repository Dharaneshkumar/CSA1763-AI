def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    dfs_order = [start_node]
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs_order.extend(dfs(graph, neighbor, visited))
    return dfs_order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs_result = dfs(graph, 'A')
print("DFS traversal order:", dfs_result)
