from collections import deque

def bfs(src, graph: dict):
    visited: set = set()
    queue: deque = deque()
    queue.append(src)

    while len(queue) > 0:
        current = queue.popleft()
        print(current)

        for element in graph[current]:
            if element not in visited:
                visited.add(element) # element will be visited (i promise)
                queue.append(element)

def main():
    graph: dict = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'E': ['G'],
        'D': [],
        'G': ['E'],
        'F': [],
    }
    bfs('A', graph)

if __name__ == "__main__":
    main()
