from binary_tree_garrido import BinaryTreeGarrido, TreeNode
from graph_garrido import GraphGarrido


def main():
    print("==========================================")
    print(" ASSESSMENT 3.4 & 3.6: NON-LINEAR DATA STRUCTURE")
    print(" Student: JED GARRIDO")
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

    # 2. Graph Execution (BFS and DFS)
    print("--- 2. GRAPH STRUCTURE ---")
    graph = GraphGarrido()
    edges = [('G', 'A'), ('A', 'R1'), ('R1', 'R2'), ('R2', 'I'), ('I', 'D'), ('D', 'O')]

    for src, dest in edges:
        graph.add_edge(src, dest)

    graph.display_graph()
    print()
    graph.bfs('G')
    graph.dfs('G')
    print("\n==========================================")


if __name__ == "__main__":
    main()