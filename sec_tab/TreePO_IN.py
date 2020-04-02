# Construct a Binary Tree from PostOrder and InOrder
# Given PostOrder and Inorder traversals, construct the tree.
# Input :
# in[]   = {4, 8, 2, 5, 1, 6, 3, 7}
# post[] = {8, 4, 5, 2, 6, 7, 3, 1}
#
# Output : Root of below tree
#          1
#         / \
#      2       3
#     /  \    / \
#     4   5   6  7
#     \
#      8
"""
We have already discussed construction of tree
from Inorder and PreOrder traversals. The idea is similar.

Let us see the process of constructing tree from
in[] = {4, 8, 2, 5, 1, 6, 3, 7} and
post[] = {8, 4, 5, 2, 6, 7, 3, 1}

1) We first find the last node in post[]. The last node is “1”, we know this value is
root as root always appear in the end of postOrder traversal.

2) We search “1” in in[] to find left and right subtrees of root. Everything on
left of “1” in in[] is in left subtree and everything on right is in right subtree.

            1
         /    \
[4, 8, 2, 5]  [6, 3, 7]

3) We recur the above process for following two.
….b) Recur for in[] = {6, 3, 7} and post[] = {6, 7, 3}
…….Make the created tree as right child of root.
….a) Recur for in[] = {4, 8, 2, 5} and post[] = {8, 4, 5, 2}.
…….Make the created tree as left child of root.

Below is the implementation of above idea. One important observation is, we recursively call
for right subtree before left subtree as we decrease index of postOrder index whenever we
create a new node.
"""


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def preOrder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


# Driver code
def BuildRecurRightLeft(InArray, PostArray, inStart, inEnd, pIndexList):
    if inStart > inEnd:
        return None
    node = newNode(PostArray[pIndexList[0]])
    pIndexList[0] -= 1
    # means node has no children
    if inStart == inEnd:
        return node
    iIndex = search(InArray, inStart, inEnd, node.data)
    # iIndex = InArray.index(node.data)

    # Using index in Inorder traversal,  construct left and right subtrees
    node.right = BuildRecurRightLeft(InArray, PostArray, iIndex + 1, inEnd, pIndexList)

    node.left = BuildRecurRightLeft(InArray, PostArray, inStart, iIndex - 1, pIndexList)

    return node


def buildTree(InArray, PostArray, ln):
    if ln == 0:
        return
    pIndexList = [ln - 1]
    return BuildRecurRightLeft(InArray, PostArray, 0, ln - 1, pIndexList)


# Optimized approach: We can optimize the above solution using hashing (unordered_map in C++
# or HashMap in Java). We store indexes of inorder traversal in a hash table. So that search
# can be done O(1) time
# element and its index as value in dictionary #
"""
just we have to send that map every time in recursive function and where we are searching for 
element in in order Array we can get its index using hash map or dictionary in O(1) time 
then overall time Complexity will reduce from O(n2) to new Time Complexity : O(n)
 """


def search(arr, startIndex, endIndex, value):
    while startIndex <= endIndex:
        if arr[startIndex] == value:
            return startIndex
        elif arr[endIndex] == value:
            return endIndex
        else:
            startIndex += 1
            endIndex -= 1


if __name__ == '__main__':
    In = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    n = len(In)

    root = buildTree(In, post, n)

    print("PreOrder of the constructed tree :")
    preOrder(root)
    # print(search(In, 0, len(In) - 1, 2))
