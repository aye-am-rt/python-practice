# In this article we will see a recursive solution without finding the height or depth. The idea
# is that while traversing the nodes compare the level of the node with max_level (Maximum level
# till the current node). If the current level exceeds the maximum level, update the max_level as current
# level. If the max level and current level are same, add the root data to current sum otherwise if level is
# less than max_level, do nothing.
import sys

sumAtMaxDepth = [0]
max_level = [-sys.maxsize + 1]


class createNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumOfNodesAtMaxDepth(rtNode, level):
    if not rtNode:
        return

    if level > max_level[0]:
        sumAtMaxDepth[0] = rtNode.data
        max_level[0] = level

    elif level == max_level[0]:
        sumAtMaxDepth[0] += rtNode.data

    sumOfNodesAtMaxDepth(rtNode.left, level + 1)
    sumOfNodesAtMaxDepth(rtNode.right, level + 1)


if __name__ == '__main__':
    # Driver Code 
    root = createNode(1)
    root.left = createNode(2)
    root.right = createNode(3)
    root.left.left = createNode(4)
    root.left.right = createNode(5)
    root.right.left = createNode(6)
    root.right.right = createNode(7)

    sumOfNodesAtMaxDepth(root, 0)

    print(sumAtMaxDepth[0])
