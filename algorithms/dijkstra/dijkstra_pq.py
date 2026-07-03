import heapq

def dijkstra(src: str, dst: str, graph: dict) -> list:
    if src not in graph:
        raise ValueError(f"The source node \'{src}\' is not found in the given graph!")
    if dst not in graph:
        raise ValueError(f"The destination node \'{dst}\' is not found in the given graph!")

    costs: dict = { node: float('inf') for node in graph.keys() }
    previous_nodes: dict = { node: None for node in graph.keys() }

    costs[src] = 0

    pq = [(0, src)]
    visited: set = set()

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node == dst:
            break

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbour, weight in graph[current_node]:
            new_cost = current_cost + weight
            if new_cost < costs[neighbour]:
                costs[neighbour] = new_cost
                previous_nodes[neighbour] = current_node
                heapq.heappush(pq, (new_cost, neighbour))

    # watch out for unreachable nodes:
    if costs[dst] == float('inf'):
        raise ValueError(f"The destination node {dst} is not reachable!")

    # construct the path:
    path = []
    current = dst
    while current != None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path

def main() -> None:
    graph: dict = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 5), ('E', 10), ('C', 1)],
        'C': [('F', 7), ('B', 3), ('A', 2)],
        'D': [('G', 6), ('B', 5)],
        'E': [('G', 1), ('B', 10)],
        'F': [('G', 3), ('C', 7)],
        'G': [('E', 1), ('C', 4)],
        'H': [],
    }
    print(dijkstra('A', 'F', graph))

if __name__ == "__main__":
    main()
