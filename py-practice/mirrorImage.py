class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def print_tree_elements(node):
    if node is None:
        return
    print_tree_elements(node.left)
    print(node.key, end=" ")
    print_tree_elements(node.right)


def make_mirror_tree(root):
    if root is None:
        return
    else:
        temp_node = root
    make_mirror_tree(root.left)
    make_mirror_tree(root.right)

    temp_node = root.left
    root.left = root.right
    root.right = temp_node


if __name__ == "__main__":
    root = BinaryTree(56)
    root.left = BinaryTree(98)
    root.right = BinaryTree(33)
    root.left.left = BinaryTree(512)
    root.left.right = BinaryTree(258)
    print("Traversing the primary tree")
    print_tree_elements(root)
    make_mirror_tree(root)
    print("\nprinting the mirrored tree")
    print_tree_elements(root)
