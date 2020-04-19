# Flatten a binary tree into linked list | Set-3
# Given a binary tree, flatten it into linked list in-place. Usage of auxiliary data structure is
# not allowed. After flattening, left of each node should point to NULL and right should contain
# next node in level order.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def PrintInorder(tRoot: Node):
    if tRoot is None:
        return
    PrintInorder(tRoot.left)
    print(tRoot.data, end=" ")
    PrintInorder(tRoot.right)


def FlattenBinaryTree(rtNode):
    global lastAddedNodeInList
    if not rtNode:
        return
    leftST = rtNode.left
    rightST = rtNode.right
    if rtNode != lastAddedNodeInList:
        lastAddedNodeInList.right = rtNode
        lastAddedNodeInList.left = None
        lastAddedNodeInList = rtNode
    FlattenBinaryTree(leftST)
    FlattenBinaryTree(rightST)
    if not leftST and not rightST:
        lastAddedNodeInList = rtNode


if __name__ == '__main__':
    # Build the tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right = Node(5)
    root.right.right = Node(6)

    # Print the inorder traversal of the
    # original tree
    print("Original inorder traversal : ", end="")
    PrintInorder(root)
    print("")
    # Global variable to maintain the
    # last node added to the linked list
    lastAddedNodeInList = root
    # Flatten the binary tree, at the beginning
    # root node is the only node in the list
    FlattenBinaryTree(root)
    # Print the inorder traversal of the flattened
    # binary tree
    print("Flattened inorder traversal : ", end="")
    PrintInorder(root)

    st = "ABBAtyssfdf"
    rst = ''.join(reversed(st))
    print("\n", rst)
