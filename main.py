from collections import deque


class TreeNode:
    """Represents a node in the Binary Tree."""

    def __init__(self, data: str):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeGarrido:
    """Binary Tree construction and traversals for GARRIDO."""

    @staticmethod
    def pre_order(root):
        if root is None:
            return
        print(root.data, end=" ")
        BinaryTreeGarrido.pre_order(root.left)
        BinaryTreeGarrido.pre_order(root.right)

    @staticmethod
    def in_order(root):
        if root is None:
            return
        BinaryTreeGarrido.in_order(root.left)
        print(root.data, end=" ")
        BinaryTreeGarrido.in_order(root.right)

    @staticmethod
    def post_order(root):
        if root is None:
            return
        BinaryTreeGarrido.post_order(root.left)
        BinaryTreeGarrido.post_order(root.right)
        print(root.data, end=" ")


class GraphGarrido:
    """Undirected Graph representation and BFS traversal for GARRIDO."""

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


def main():
    print("==========================================")
    print(" ASSESSMENT 3.4: NON-LINEAR DATA STRUCTURE")
    print(" Student: GARRIDO")
    print("==========================================\n")

    # 1. Binary Tree Execution
    print("--- 1. BINARY TREE STRUCTURE ---")
    root = TreeNode('G')
    root.left = TreeNode('A')
    root.right = TreeNode('R')

    root.left.left = TreeNode('R')
    root.left.right = TreeNode('I')

    root.right.left = TreeNode('D')
    root.right.right = TreeNode('O')

    print("Pre-Order (Root -> Left -> Right):  ", end="")
    BinaryTreeGarrido.pre_order(root)
    print()

    print("In-Order (Left -> Root -> Right):   ", end="")
    BinaryTreeGarrido.in_order(root)
    print()

    print("Post-Order (Left -> Right -> Root): ", end="")
    BinaryTreeGarrido.post_order(root)
    print("\n")

    # 2. Graph Execution
    print("--- 2. GRAPH STRUCTURE ---")
    graph = GraphGarrido()
    edges = [('G', 'A'), ('A', 'R'), ('R', 'I'), ('I', 'D'), ('D', 'O')]

    for src, dest in edges:
        graph.add_edge(src, dest)

    graph.display_graph()
    print()
    graph.bfs('G')
    print("\n==========================================")


if __name__ == "__main__":
    main()