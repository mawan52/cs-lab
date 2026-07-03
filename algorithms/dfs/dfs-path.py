# This implementation extends DFS to also return a path to the destination
# node starting from the source node.
# 
# 1. Pick a route -> 2.
# 2. keep going until u reach a dead end or alrdy visited node -> 3.
#       What is a dead end?
#       > i guess when a node doesnt have any more unvisited nodes
# 3. backtrack to last node with unvisited adjacent neighbors -> 1.


def dfs(graph: dict, src: str, dst: str):
    path: list = []
    visited: set = set()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def dfs_worker(graph: dict, src: str, dst: str, path: list, visited: set) -> None | list:
        # VISIT NODE
        path.append(src)
        visited.add(src)

        # FINISH IF DESTINATION REACHED
        if src == dst:
            return path

        for neighbor in graph[src]:
            if neighbor in visited:
                continue
            if dfs_worker(graph, neighbor, dst, path, visited):
                return path

        # BACKTRACK
        path.pop()
        return None
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    return dfs_worker(graph, src, dst, path, visited)


def main():
    graph = {
        'A': set("BE"),
        'B': set("DAC"),
        'C': set("B"),
        'D': set("B"),
        'E': set("A"),
    }
    print(dfs(graph, 'A', 'A'))


if __name__ == "__main__":
    main()
