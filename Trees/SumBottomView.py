# Sum of nodes in bottom view of Binary Tree
# Given a binary tree, the task is to print the sum of nodes in bottom view of the given Binary Tree.
# Bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.

"""Approach: The idea is to use a queue.

Put tree nodes in a queue for the level order traversal
Start with the horizontal distance(hd) 0 of the root node, keep on adding left child to queue along
with the horizontal distance as hd-1 and right child as hd+1.
Use a map to store the hd value(as key) and the last node(as pair) having the corresponding hd value.
Every time, we encounter a new horizontal distance or an existing horizontal distance put the node
data for the horizontal distance as key. For the first time it will add to the map, next time it
will replace the value. This will make sure that the bottom most element for that horizontal
distance is present in the map.
Finally, traverse the map and calculate the sum of all of the elements."""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = None


def SumOfBottomView(rtNode: Node):
    if not rtNode:
        return 0
    hd, totalSum = 0, 0
    rtNode.hd = hd
    hdDict = {}
    q = [rtNode]
    while len(q):
        tempNode = q.pop(0)
        hd = tempNode.hd
        hdDict[hd] = tempNode.data

        if tempNode.left:
            tempNode.left.hd = hd - 1
            q.append(tempNode.left)
        if tempNode.right:
            tempNode.right.hd = hd + 1
            q.append(tempNode.right)

    for hdKey in hdDict:
        totalSum += hdDict[hdKey]
    return totalSum


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    print("sum of bottom view of binary try is ==", end=" ")
    print(SumOfBottomView(root))
