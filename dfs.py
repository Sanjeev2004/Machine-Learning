from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Queue to store (current_node, path_to_current_node)
    queue = deque([(start, [start])])
    
    # Set to keep track of visited nodes
    visited = set()
    
    while queue:
        current_node, path = queue.popleft()
        
        if current_node == goal:
            return path
        
        if current_node not in visited:
            visited.add(current_node)
            
            # Add neighbors to the queue
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    return None  # No path found

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

start = 0
goal = 5
shortest_path = bfs_shortest_path(graph, start, goal)
print("Shortest path:", shortest_path)
