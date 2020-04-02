class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def InsertInBST(rt, val):
    if rt is None:
        return Node(val)
    if rt.data < val:
        rt.right = InsertInBST(rt.right, val)
    elif rt.data > val:
        rt.left = InsertInBST(rt.left, val)
    return rt


# This function finds predecessor and successor of key in BST
# It sets pre and suc as predecessor and successor respectively
def findPreSuc(rt, target):
    if rt is None:
        return
    if rt.data == target:
        # the maximum value in left subtree is predecessor
        if rt.left is not None:
            tmp = rt.left
            while tmp.right:
                tmp = tmp.right
            findPreSuc.pre = tmp

        # the minimum value in right subtree is successor
        if rt.right is not None:
            tmp = rt.right
            while tmp.left:
                tmp = tmp.left
            findPreSuc.suc = tmp
        return

    # If key is smaller than root's key, go to left subtree
    if rt.data > target:
        findPreSuc.suc = rt
        findPreSuc(rt.left, target)
    # If key is greater than root's key, go to right subtree
    if rt.data < target:
        findPreSuc.pre = rt
        findPreSuc(rt.right, target)


def InOrderTraversal(root):
    # if root is None
    if not root:
        return
    InOrderTraversal(root.left)
    print(root.data, end=" ")
    InOrderTraversal(root.right)


if __name__ == '__main__':
    root = Node(34)
    root = InsertInBST(root, 5)
    root = InsertInBST(root, 12)
    root = InsertInBST(root, 55)
    root = InsertInBST(root, 3)
    root = InsertInBST(root, 6)
    root = InsertInBST(root, 2)
    root = InsertInBST(root, 543)
    root = InsertInBST(root, 95)
    root = InsertInBST(root, 21)

    # Static variables of the function findPreSuc
    findPreSuc.pre = None
    findPreSuc.suc = None
    key = 95
    print("Inorder Order traversal of tree==> left--root--right")
    InOrderTraversal(root)
    findPreSuc(root, key)

    if findPreSuc.pre is not None:
        print("\nPredecessor is", findPreSuc.pre.data)

    else:
        print("No Predecessor")

    if findPreSuc.suc is not None:
        print("Successor is", findPreSuc.suc.data)
    else:
        print("No Successor")
