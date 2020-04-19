# Convert a given Binary Tree to Doubly Linked List | Set 3
#
# In this post, a third solution is discussed which seems to be the simplest of all. The idea is to
# do inorder traversal of the binary tree. While doing inorder traversal, keep track of the
# previously visited node in a variable say prev. For every visited node, make it next of prev and
# previous of this node as prev.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BtToDLL:
    prev = None  # static variable # Initialize previously visited node as NULL. This is
    # static so that the same value is accessible in all recursive calls

    def __init__(self):
        self.root = self.head = None

    # rtNode is root node of binary tree
    def BTtoDLList(self, rtNode: Node):
        if rtNode is None:
            return

        self.BTtoDLList(rtNode.left)
        if self.prev is None:
            self.head = rtNode
        else:
            rtNode.left = self.prev
            self.prev.right = rtNode

        self.prev = rtNode
        self.BTtoDLList(rtNode.right)

    @staticmethod
    def print_list(head: Node):
        print('Extracted Double Linked list is:')
        while head is not None:
            print(head.data, end=' ')
            head = head.right


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
    tree = BtToDLL()
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
