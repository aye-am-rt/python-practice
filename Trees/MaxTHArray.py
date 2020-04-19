"""
maximum height of the binary search tree created from the given array
Given an array arr[] of N integers, the task is to make two binary search trees.
One while traversing from the left side of the array and another while traversing from the right
and find which tree has a greater height.

Approach:

Create a binary search tree while inserting the nodes starting from the first element of the array
till the last and find the height of this created tree say leftHeight.
Create another binary search tree while inserting the nodes starting from the last element of the
array till the first and find the height of this created tree say rightHeight.
Print the maximum of these calculated heights i.e. max(leftHeight, rightHeight)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def InsertInBST(value, root: Node = None):
    if root is None:
        return Node(value)

    elif value > root.data:
        root.right = InsertInBST(value, root.right)
    elif value < root.data:
        root.left = InsertInBST(value, root.left)
    return root


def findDepth(root: Node):
    if root is None:
        return 0
    else:
        lHeight = findDepth(root.left)
        rHeight = findDepth(root.right)

        if lHeight > rHeight:
            return lHeight + 1
        else:
            return rHeight + 1


def printInorder(root: Node):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end="  ")
    printInorder(root.right)


def maxHeight(arr, ln):
    rt1 = InsertInBST(arr[0])
    rt2 = InsertInBST(arr[ln - 1])
    for i in range(1, ln):
        rt1 = InsertInBST(arr[i], rt1)
        rt2 = InsertInBST(arr[ln - i - 1], rt2)

    print("first tree inorder = ")
    printInorder(rt1)
    print("\nsecond tree inorder = ")
    printInorder(rt2)

    h1 = findDepth(rt1) - 1
    h2 = findDepth(rt2) - 1
    print(f"\nh1= {h1} and h2= {h2}")

    if h1 > h2:
        print(f"max height can be achieved by left to right insertion i.e= {h1}")
    else:
        print(f"max height can be achieved by right to left insertion i.e= {h2}")


if __name__ == "__main__":
    a = [10, 9, 19, 18, 2, 3, 4, 11, 12, 13, 41]
    n = len(a)
    maxHeight(a, n)
