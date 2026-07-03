# This is a standard implementation of recursive DFS in python.
def dfs(src, graph:dict) -> None:
    visited:set = set()

    # # # # # # # # # # # # # # # # # # # # #
    def dfs_worker(src, graph:dict):
        visited.add(src)
        print(src)
        for neighbour in graph[src]:
            if neighbour not in visited:
                dfs_worker(neighbour, graph)
    # # # # # # # # # # # # # # # # # # # # #

    dfs_worker(src, graph)

def main():
    graph:dict = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'E': ['G'],
        'D': [],
        'G': [],
        'F': [],
    }
    dfs('A', graph)

if __name__ == "__main__":
    main()
