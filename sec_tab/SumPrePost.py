"""Replace each node in binary tree with the sum of its inorder predecessor and successor
Given a binary tree containing n nodes. The problem is to replace each node in the binary
 tree with the sum of its inorder predecessor and inorder successor.

 ===========================================================================

 Create an array arr. Store 0 at index 0. Now, store the inorder traversal of tree in the array arr.
 Then, store 0 at last index. 0’s are stored as inorder predecessor of leftmost leaf and inorder
 successor of rightmost leaf is not present. Now, perform inorder traversal and while traversing
 node replace node’s value with arr[i-1] + arr[i+1] and then increment i. In the beginning initialize
  i = 1. For an element arr[i], the values arr[i-1] and arr[i+1] are its inorder predecessor and
  inorder successor respectively.

 """


class getNode:
    def __init__(self, data):
        # put in the data
        self.data = data
        self.left = self.right = None


def storeInorderTraversal(root, arr):
    # if root is None
    if not root:
        return

    # first recur on left child
    storeInorderTraversal(root.left, arr)

    # then store the root's data in 'arr'
    arr.append(root.data)

    # now recur on right child
    storeInorderTraversal(root.right, arr)


def preOrderTraversal(root):
    # if root is None
    if not root:
        return

    # first print the data of node
    print(root.data, end=" ")

    # then recur on left subtree
    preOrderTraversal(root.left)

    # now recur on right subtree
    preOrderTraversal(root.right)


def replaceNodeWithSum(rt, arr, i):
    if not rt:
        return
    replaceNodeWithSum(rt.left, arr, i)
    rt.data = arr[i[0] - 1] + arr[i[0] + 1]
    i[0] += 1
    replaceNodeWithSum(rt.right, arr, i)


def replaceNodeWithSumUtil(rt):
    if not root:
        return
    arr = [0]
    storeInorderTraversal(root, arr)
    arr.append(0)
    i = [1]
    replaceNodeWithSum(root, arr, i)


"""
Time Complexity: O(n)
Auxiliary Space: O(n)

"""
if __name__ == '__main__':
    # binary tree formation
    root = getNode(1)
    root.left = getNode(2)
    root.right = getNode(3)
    root.left.left = getNode(4)
    root.left.right = getNode(5)
    root.right.left = getNode(6)
    root.right.right = getNode(7)

    print("PreOrder Traversal before", "tree modification:")
    preOrderTraversal(root)

    replaceNodeWithSumUtil(root)
    print()
    print("PreOrder Traversal after", "tree modification:")
    preOrderTraversal(root)
