# Construct a Binary Search Tree from given postorder
# Given postorder traversal of a binary search tree, construct the BST.
#
# Method 2 ( O(n) time complexity )
# The trick is to set a range {min .. max} for every node. Initialize the range as
# {INT_MIN .. INT_MAX}. The last node will definitely be in range, so create root node. To construct
# the left subtree, set the range as {INT_MIN …root->data}. If a values is in the range
# {INT_MIN .. root->data}, the values is part part of left subtree. To construct the right subtree,
# set the range as {root->data .. INT_MAX}.
#
# Following code is used to generate the exact Binary Search Tree of a given post order traversal.

"""  The last element of postOrder traversal is always root.   We first construct the root.
## Then we find the index of last element which is smaller than root.##
Let the index be ‘i’. The values between 0 and ‘i’ are part of left subtree, and the values between
‘i+1’ and ‘n-2’ are part of right subtree. Divide given post[] at index “i” and recur
for left and right sub-trees."""
# from sec_tab.MaxTHArray import printInorder

INT_MIN = -2 ** 31
INT_MAX = 2 ** 31


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# O(n) time complexity
def MakeRecPostRoot(PostArray, indexArr, key, minn, maxx, lArr):
    if indexArr[0] < 0:
        return None

    rt = None
    if minn < key < maxx:
        rt = newNode(key)
        indexArr[0] -= 1
        if indexArr[0] > -1:
            rt.right = MakeRecPostRoot(PostArray, indexArr, PostArray[indexArr[0]], key, maxx, lArr)
            rt.left = MakeRecPostRoot(PostArray, indexArr, PostArray[indexArr[0]], minn, key, lArr)
    return rt


# O(n) time complexity
def constructTree(PostArray, lArr):
    if lArr == 0:
        return
    indexArr = [lArr - 1]
    key = PostArray[indexArr[0]]
    minn = INT_MIN
    maxx = INT_MAX
    return MakeRecPostRoot(PostArray, indexArr, key, minn, maxx, lArr)


def printInorder(rtNode):
    if not rtNode:
        return
    printInorder(rtNode.left)
    print(rtNode.data, end="  ")
    printInorder(rtNode.right)


if __name__ == '__main__':
    post = [1, 7, 5, 50, 40, 10]
    size = len(post)
    root = constructTree(post, size)

    print("Inorder traversal of the", "constructed tree: ")
    printInorder(root)

#
# Therefore, following combination can uniquely identify a tree.
#
# Inorder and Preorder.
# Inorder and Postorder.
# Inorder and Level-order.
#
# And following do not.
# Postorder and Preorder.
# Preorder and Level-order.
# Postorder and Level-order.
#
# For example, Preorder, Level-order and Postorder traversals are same for the trees given in
# above diagram.
#
# So, even if three of them (Pre, Post and Level) are given, the tree can not be constructed
