def dijkstra(src: str, dst: str, graph: dict):
    if src not in graph or dst not in graph:
        return None
    
    # create unvisited set
    unvisited = set( graph.keys() )

    # create node distance dictionary
    # and its helper functions
    node_info: dict = { i : [ float('inf'), '' ] for i in graph.keys() }

    def set_cost(node, cost):
        node_info[node][0] = cost

    def get_cost(node):
        return node_info[node][0]

    def set_prevnode(node, prevnode):
        node_info[node][1] = prevnode

    def get_prevnode(node) -> str:
        return node_info[node][1]

    set_cost(src, 0)
    current:str = src

    while len(unvisited) > 0:
        # check neighbors:
        for (neighbour, cost) in graph[current]:
            cost = get_cost(current) + cost
            if cost < get_cost(neighbour):
                set_cost(neighbour, cost)
                set_prevnode(neighbour, current)
        unvisited.remove(current)
        if len(unvisited) <= 0: break
        current = sorted(unvisited, key=lambda x: get_cost(x))[0]

    if get_cost(dst) == float('inf'):
        return None

    # get the path:
    path:list = list()
    node:str = dst
    path.append(node)
    while node != src:
        prev_node = get_prevnode(node)
        path.append(prev_node)
        node = prev_node
    path.reverse()
    return path, get_cost(dst)
    
def main():
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
