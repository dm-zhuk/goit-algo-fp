'''
Дерева, алгоритм Дейкстри
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.
'''


import heapq
from collections import defaultdict
def create_graph():
    graph = defaultdict(list)
    edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
    ]
    nodes = {"A", "B", "C", "D", "E"}
    for src, dst, weight in edges:
        graph[src].append((dst, weight))
        graph[dst].append((src, weight))
    return graph, nodes

def dijkstra(graph, nodes, start):
    distances = {node: float('infinity') for node in nodes}
    distances[start] = 0
    paths = {node: [start] for node in nodes}
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    visited = set()

    while pq:
        # Get node with smallest distance
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        # Check neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
                
            new_distance = current_distance + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(pq, (new_distance, neighbor))
    
    return distances, paths

# Test algorithm
graph, nodes = create_graph()
start_node = "A"
distances, paths = dijkstra(graph, nodes, start_node)

print(f"Shortest paths from {start_node}:")
for node in sorted(nodes):
    if node == start_node:
        continue
    print(f"To {node}: Distance = {distances[node]}, Path = {' -> '.join(paths[node])}")