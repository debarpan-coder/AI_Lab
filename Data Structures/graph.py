from dsa_queue import CircularQueue
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def display(self):
        for node, edges in self.graph.items():
            print(f"{node}: {edges}")
            
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue=CircularQueue(10)
        queue.enqueue(start)
        visited.add(start)
        node = queue.dequeue()
        while node != -1:
            print(node, end=' ')
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
            node = queue.dequeue()

    def iddfs(self, start, max_depth):
        for depth in range(max_depth):
            self._iddfs_helper(start, depth)

    def _iddfs_helper(self, node, depth, visited=None):
        if visited is None:
            visited = set()
        if depth == 0:
            print(node, end=' ')
            return True
        elif depth > 0:
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    if self._iddfs_helper(neighbor, depth - 1, visited):
                        print(neighbor, end=' ')
            visited.remove(node)
        return False

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(4, 7)
g.add_edge(4, 6)
g.add_edge(4, 3)
g.add_edge(3, 5)
g.add_edge(5, 6)

g.display()

print("BFS:")
g.bfs(1)
print("\nDFS:")
g.dfs(1)
print("\nIDDFS:")
g.iddfs(1,2)
