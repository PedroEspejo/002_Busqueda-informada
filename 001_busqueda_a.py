import heapq


def a_star_search(graph, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            path = reconstruct_path(came_from, current_node)
            return path
        
        for neighbor, cost in graph[current_node]:
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
    
    return None


def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.insert(0, current_node)
    return path


# Ejemplo
def heuristic(node, goal):
    # Esta es una heurística simple que devuelve la distancia entre los nodos
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((0, 2), 1)],
    (0, 2): [((0, 1), 1), ((1, 2), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1), ((1, 2), 1)],
    (1, 2): [((1, 1), 1), ((0, 2), 1)]
}

start_node = (0, 0)
goal_node = (1, 2)
path = a_star_search(graph, start_node, goal_node)
print("Camino encontrado:", path)