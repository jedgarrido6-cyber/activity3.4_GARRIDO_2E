class TreeNode:
    """Represents a node in the Binary Tree for JED GARRIDO."""
    def __init__(self, data: str):
        self.data = data
        self.left = None
        self.right = None


class DFSTreeGarrido:
    """DFS Traversals (PreOrder, InOrder, PostOrder) for JED GARRIDO Binary Tree."""

    @staticmethod
    def pre_order(root):
        """Root -> Left -> Right"""
        if root is None:
            return []
        return [root.data] + DFSTreeGarrido.pre_order(root.left) + DFSTreeGarrido.pre_order(root.right)

    @staticmethod
    def in_order(root):
        """Left -> Root -> Right"""
        if root is None:
            return []
        return DFSTreeGarrido.in_order(root.left) + [root.data] + DFSTreeGarrido.in_order(root.right)

    @staticmethod
    def post_order(root):
        """Left -> Right -> Root"""
        if root is None:
            return []
        return DFSTreeGarrido.post_order(root.left) + DFSTreeGarrido.post_order(root.right) + [root.data]


if __name__ == "__main__":
    root = TreeNode('G')
    root.left = TreeNode('A')
    root.right = TreeNode('R')

    root.left.left = TreeNode('R')
    root.left.right = TreeNode('I')

    root.right.left = TreeNode('D')
    root.right.right = TreeNode('O')

    print("==========================================")
    print(" ASSESSMENT 3.6: DFS METHODS IN TREE")
    print(" Student: JED GARRIDO")
    print("==========================================\n")

    print("PreOrder  (Root -> Left -> Right):", " -> ".join(DFSTreeGarrido.pre_order(root)))
    print("InOrder   (Left -> Root -> Right):", " -> ".join(DFSTreeGarrido.in_order(root)))
    print("PostOrder (Left -> Right -> Root):", " -> ".join(DFSTreeGarrido.post_order(root)))
    print("\n==========================================")