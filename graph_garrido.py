from collections import deque


class GraphGarrido:
    """Undirected Graph representation, BFS, and DFS traversal for JED GARRIDO."""

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

    def dfs(self, start_node: str):
        visited = set()
        print(f"DFS Traversal starting from '{start_node}': ", end="")

        def _dfs_helper(node):
            visited.add(node)
            print(node, end=" ")

            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    _dfs_helper(neighbor)

        _dfs_helper(start_node)
        print()


if __name__ == "__main__":
    graph = GraphGarrido()
    edges = [('G', 'A'), ('A', 'R1'), ('R1', 'R2'), ('R2', 'I'), ('I', 'D'), ('D', 'O')]

    for src, dest in edges:
        graph.add_edge(src, dest)

    print("=== GRAPH STRUCTURE (JED GARRIDO) ===")
    graph.display_graph()
    print()
    graph.bfs('G')
    graph.dfs('G')