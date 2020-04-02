# Write a Program to Find the Maximum Depth or Height of a Tree
# Recursively calculate height of left and right subtrees of a node and assign height to the node
# as max of the heights of two children plus 1. See below pseudo code and program for details.
#
# Algorithm:
# maxDepth()
# 1. If tree is empty then return 0
# 2. Else
#   (a) Get the max depth of left subtree recursively  i.e.,
# call maxDepth( tree->left-subtree)
#   (a) Get the max depth of right subtree recursively  i.e.,
# call maxDepth( tree->right-subtree)
#   (c) Get the max of max depths of left and right
# subtrees and add 1 to it for the current node.
# max_depth = max(max dept of left subtree,max depth of right subtree)+ 1
#   (d) Return max_depth


class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


def FindMaxDepth(root: Node):
    if root is None:
        return 0
    else:
        lHeight = FindMaxDepth(root.left)
        rHeight = FindMaxDepth(root.right)

        if lHeight > rHeight:
            return lHeight + 1
        else:
            return rHeight + 1


rt = Node(5)
rt.left = Node(2)
rt.right = Node(3)
rt.left.left = Node(4)
rt.left.right = Node(5)

print(f"Height of tree is {FindMaxDepth(rt)}")
