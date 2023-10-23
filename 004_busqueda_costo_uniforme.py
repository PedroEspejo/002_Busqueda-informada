import heapq

def ucs_informed_search(graph, start, goal, heuristic):
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node == goal:
            return cost
        
        if node in visited:
            continue

        visited.add(node)

        for neighbor, neighbor_cost in graph[node].items():
            if neighbor not in visited:
                total_cost = cost + neighbor_cost + heuristic(neighbor, goal)
                heapq.heappush(queue, (total_cost, neighbor))

# Ejemplo de uso
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 15},
    'C': {'A': 10, 'E': 20},
    'D': {'B': 15, 'F': 5},
    'E': {'C': 20, 'F': 10},
    'F': {'D': 5, 'E': 10}
}

def euclidean_heuristic(node, goal):
    coordinates = {
        'A': (0, 0),
        'B': (3, 2),
        'C': (1, 5),
        'D': (6, 3),
        'E': (2, 7),
        'F': (7, 7)
    }
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

start_node = 'A'
goal_node = 'F'

cost = ucs_informed_search(graph, start_node, goal_node, euclidean_heuristic)
print("Costo de la ruta más corta:", cost)
