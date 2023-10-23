def greedy_search(graph, start, goal):
    open_list = [start]
    came_from = {}
    
    while open_list:
        current_node = open_list.pop(0)
        
        if current_node == goal:
            path = reconstruct_path(came_from, current_node)
            return path
        
        for neighbor, _ in graph.get(current_node, []):
            if neighbor not in came_from:
                came_from[neighbor] = current_node
                open_list.append(neighbor)
    
    return None

def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.insert(0, current_node)
    return path

# Ejemplo de uso
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('D', 8)],
    'C': [('A', 3), ('D', 2)],
    'D': [('B', 8), ('C', 2)]
}
start_node = 'A'
goal_node = 'D'
path = greedy_search(graph, start_node, goal_node)

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró un camino.")
