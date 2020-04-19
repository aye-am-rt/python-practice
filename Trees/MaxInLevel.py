"""Find the maximum node at a given level in a binary tree
Given a Binary Tree and a Level. The task is to find the node with the maximum value at
 that given level."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def FindMaxAtLevel(root, level):
    if root is None:
        return 0
    if level == 0:
        return root.data

    lMax = FindMaxAtLevel(root.left, level-1)
    rMax = FindMaxAtLevel(root.right, level-1)

    return max(lMax, rMax)


# Driver Code
if __name__ == '__main__':
    """  
    Let us create Binary Tree shown 
    in above example """
    rt = Node(45)
    rt.left = Node(46)
    rt.left.left = Node(18)
    rt.left.left.left = Node(16)
    rt.left.left.right = Node(23)
    rt.left.right = Node(17)
    rt.left.right.left = Node(24)
    rt.left.right.right = Node(21)
    rt.right = Node(15)
    rt.right.left = Node(22)
    rt.right.left.left = Node(37)
    rt.right.left.right = Node(41)
    rt.right.right = Node(19)
    rt.right.right.left = Node(49)
    rt.right.right.right = Node(29)
    lvl = 3
    # rt = Node(1)
    # rt.left = Node(2)
    # rt.right = Node(3)
    # rt.left.left = Node(4)
    # rt.left.right = Node(5)
    print(FindMaxAtLevel(rt, lvl))
