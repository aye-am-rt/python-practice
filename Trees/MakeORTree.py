""" Convert a given Binary tree to a tree that holds Logical OR property
Given a Binary Tree (Every node has at most 2 children) where each node has value either 0 or 1.
The task is to convert the given Binary tree to a tree that holds Logical OR property, i.e.,
each node value should be the logical OR between its children."""

# Explanation:
# Given Tree
#       1
#      / \
#     1    0
#    / \   / \
#   0   1  1  1
#
# After Processing
#         1
#       /    \
#      1       1
#     /  \    /  \
#     0   1   1   1

"""
Approach:
The idea is to traverse given binary tree in post order fashion because in post order traversal 
both the children of the root has already been visited before the root itself.
For each node check (recursively) if the node has one children then we don’t have any need to 
check else if the node has both its child then simply update the node data with the 
logic or of its child data.
"""


class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printInorder(root):
    if (root == None):
        return

    # First recur on left child
    printInorder(root.left)

    # Then print the data of node
    print(root.data, end=" ")

    # Now recur on right child
    printInorder(root.right)


# Driver Code
def convertTreeInOR(rtNode):
    if not rtNode:
        return
    convertTreeInOR(rtNode.left)
    convertTreeInOR(rtNode.right)
    if rtNode.left and rtNode.right:
        rtNode.data = rtNode.left.data | rtNode.right.data


if __name__ == '__main__':
    root = newNode(0)
    root.left = newNode(1)
    root.right = newNode(0)
    root.left.left = newNode(0)
    root.left.right = newNode(1)
    root.right.left = newNode(1)
    root.right.right = newNode(1)

    convertTreeInOR(root)
    printInorder(root)
