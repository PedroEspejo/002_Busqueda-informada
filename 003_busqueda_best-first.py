import heapq

def best_first_search(graph, start, goal, heuristic):
    queue = [(heuristic(start, goal), start)]
    visited = set()
    parent = {}

    while queue:
        _, node = heapq.heappop(queue)

        if node == goal:
            return reconstruct_path(start, goal, parent)
        
        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                parent[neighbor] = node
                heapq.heappush(queue, (heuristic(neighbor, goal), neighbor))

def reconstruct_path(start, goal, parent):
    path = [goal]
    while goal != start:
        goal = parent[goal]
        path.append(goal)
    return list(reversed(path))

# Ejemplo de uso
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 15},
    }