from collections import deque


class GraphGarrido:
    """Undirected Graph representation and BFS traversal for GARRIDO (Assessment 3.3)."""

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v: str):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, src: str, dest: str):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def display_graph(self):
        print("Adjacency List Representation:")
        for vertex, neighbors in self.adj_list.items():
            print(f"  {vertex} -> {neighbors}")

    def bfs(self, start_node: str):
        visited = {start_node}
        queue = deque([start_node])

        print(f"BFS Traversal starting from '{start_node}': ", end="")
        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()


if __name__ == "__main__":
    graph = GraphGarrido()

    # Sequential edges connecting the unique vertices of GARRIDO: G, A, R, I, D, O
    edges = [('G', 'A'), ('A', 'R'), ('R', 'I'), ('I', 'D'), ('D', 'O')]
    for src, dest in edges:
        graph.add_edge(src, dest)

    print("=== GRAPH STRUCTURE (GARRIDO) ===")
    graph.display_graph()
    print()
    graph.bfs('G')