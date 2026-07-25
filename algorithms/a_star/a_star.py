import heapq
from data.graph import graph, goal, heuristic

def a_star(src: str, dst: str, graph: dict, heuristic: dict):
    if src not in graph:
        raise ValueError(f"The source node \'{src}\' is not found in the given graph!")
    if dst not in graph:
        raise ValueError(f"The destination node \'{dst}\' is not found in the given graph!")

    costs: dict = { node: float('inf') for node in graph.keys() }
    previous_nodes: dict = { node: None for node in graph.keys() }
    visited: set = set()

    costs[src] = 0
    pq = [(heuristic[src], src)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node == dst:
            break

        if current_node in visited:
            continue

        visited.add(current_node)

        for adjacent, weight in graph[current_node]:
            new_cost = weight + costs[current_node]

            if new_cost < costs[adjacent]:
                costs[adjacent] = new_cost
                previous_nodes[adjacent] = current_node
                heapq.heappush(pq, (new_cost + heuristic[adjacent], adjacent))

    # unreachable node
    if costs[dst] == float("inf"):
        return None, float("inf")

    # reconstruct
    current = dst
    path: list = []
    while current != None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path, costs[dst]
                

def main() -> None:
    print(a_star("A", goal, graph, heuristic))

if __name__ == "__main__":
    main()
