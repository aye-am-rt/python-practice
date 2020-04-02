# In the following implementation, we traverse the tree in inorder fashion. We add nodes at the
# beginning of current linked list and update head of the list using pointer to head pointer.
# Since we insert at the beginning, we need to process leaves in reverse order. For reverse order, we
# first traverse the right subtree before the left subtree. i.e. do a
""" reverse inorder traversal."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BTtoDll:
    root, head = None, None

    def BTtoDLList(self, root: Node):
        if root is None:
            return
        self.BTtoDLList(root.right)
        root.right = self.head
        if self.head is not None:
            self.head.left = root
        self.head = root
        self.BTtoDLList(root.left)

    @staticmethod
    def print_list(head: Node):
        print('Extracted Double Linked list is:')
        while head is not None:
            print(head.data, end=' ')
            head = head.right


# Driver Code
if __name__ == '__main__':
    """ 
    Constructing below tree 
            5 
        // \\ 
        3 6 
        // \\ \\ 
        1 4 8 
    // \\ // \\ 
    0 2 7 9 
    """
    tree = BTtoDll()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)
    tree.root.right.right = Node(8)
    tree.root.left.left.left = Node(0)
    tree.root.left.left.right = Node(2)
    tree.root.right.right.left = Node(7)
    tree.root.right.right.right = Node(9)

    tree.BTtoDLList(tree.root)
    tree.print_list(tree.head)
