class TreeNode:
    """Represents a node in the Binary Tree."""

    def __init__(self, data: str):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeGarrido:
    """Binary Tree construction and traversals for GARRIDO (Assessment 3.3)."""

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


if __name__ == "__main__":
    # Constructing the Binary Tree for GARRIDO
    # Root: G | Level 1: A, R | Level 2: R, I, D, O
    root = TreeNode('G')
    root.left = TreeNode('A')
    root.right = TreeNode('R')

    root.left.left = TreeNode('R')
    root.left.right = TreeNode('I')

    root.right.left = TreeNode('D')
    root.right.right = TreeNode('O')

    print("=== BINARY TREE TRAVERSALS (GARRIDO) ===")
    print("Pre-Order (Root -> Left -> Right): ", end="")
    BinaryTreeGarrido.pre_order(root)
    print()

    print("In-Order (Left -> Root -> Right):  ", end="")
    BinaryTreeGarrido.in_order(root)
    print()

    print("Post-Order (Left -> Right -> Root): ", end="")
    BinaryTreeGarrido.post_order(root)
    print()